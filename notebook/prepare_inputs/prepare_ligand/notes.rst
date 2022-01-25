**************
Prepare ligand
**************

I need to write a script that will accept any NCAA (specified by a SMILES 
string) and produce whatever files rosetta will need to simulate that NCAA.  A 
basic outline of the process I'm envisioning:

- Parse SMILES string and identify Cα.

- Adenylate amino acid.

- Generate rotamers.

  - It might be possible to use Rosetta rotamers in some cases.

Relevant Rosetta documentation:

- https://www.rosettacommons.org/docs/latest/rosetta_basics/preparation/preparing-ligands

- https://www.rosettacommons.org/demos/latest/tutorials/prepare_ligand/prepare_ligand_tutorial

Conformer-generation software
=============================
Most of the focus in the field of conformer generation seems to be on virtual 
screening, where it is necessary to test very large numbers of molecules.  This 
leads to speed-for-accuracy trade-offs.  For my application, though, I don't 
mind spending a long time generating conformers.  Unfortunately, because the 
expensive tools aren't really discussed, it could be hard to figure out how to 
use them.

Conformer-generation in the Rosetta literature:

- [Tinberg2013]_: Manually in rosetta.
- [Dou2017]_: Omega2
- [Moretti2016]_: BCL 

  - BCL was written by Jens Meiler, who is also the last author of this paper.

https://ukqsar.org/wp-content/uploads/2017/10/03.-Matthew-Habgood-UKQSAR_conformers.pdf

RDKit:

- Uses ETKDG algorithm by default, but seems like you can basically write your 
  own distance geometry (DG) algorithm.

- https://rdkit.org/docs/GettingStartedInPython.html?highlight=etkdg#working-with-3d-molecules

Babel:

- https://open-babel.readthedocs.io/en/latest/3DStructureGen/multipleconformers.html
- Babel has two algorithms:

  - "Genetic algorithm"
  - Confab

- None of the reviews I've read have mentioned Babel, but they have mentioned 
  Confab.  So I get the impression that Babel is just an interface to other 
  algorithms, although if that's the case, I don't know what the "genetic 
  algorithm" is.

Confab:

Frog:

CSD conformer generator [Cole2018]_:

- https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/conformer.html
- Based on torsions seen in small molecule crystal structures.
- I can see these torsions being both similar to and different from those you'd 
  find in a protein binding site.
- Requires access to the proprietary CCDC database.

OpenEye Omega:

- https://docs.eyesopen.com/applications/omega/index.html
- Commercial, not sure if we have license.

MOE:

- "MD motion along low-frequency vibrational modes to move between potential
  energy basins, coupled with energy minimization."
- Commercial

2021/12/08:

I'm inclined to just use RDKit for now: it's open source and seems to be well 
regarded.  I should ask Nicole about getting access to some of the commercial 
tools, though.  I might also try to get [Gaalswyk2016]_ to work, since explicit 
MD seems like the best approach even if it's not one of the method everyone 
benchmarks against.

2021/12/20:

I finally got RDKit to "work", but its ``coordMap`` feature isn't up to the 
task of holding the whole adenylate in place.  The more atoms that are 
restrained, the more each of those atoms can move.  So I'm going to have to 
find a different approach.

I asked Emma about OpenEye Omega, but I probably won't hear back until the new 
year.  It has this feature, and I think it'll actually work because the 
algorithm is based on perturbing torsions (I think).  I don't like using closed 
source software, though.

I looked closer at [Gaalswyk2016]_.  It'll be a lot of work to do something 
like that.  I'll have to rewrite most of the code, and I'm not familiar with 
any of the tools (NAMD and VMD, mostly).  NAMD and VMD are also closed source, 
so this doesn't really solve the headaches that Omega causes.

The OpenBabel C++ API also has ways to hold atoms fixed.

2021/12/21:

I figured out that by manually setting the bounds matrix after smoothing, I can 
get RDKit to mostly respect the coordinate restraints.


Adenylate
=========
I gave some thought to the question of how much to vary the coordinates of the 
adenylate moiety between the different ligand conformers.  Ultimately, I 
decided to not vary them at all:

- If I vary the adenylate coordinates, the NCAA conformations that happen to be 
  attached to better adenylate conformations will be artificially favored.

- The above effect would make sense if there was a strong connection between 
  the NCAA and adenylate conformations, but since the adenylate conformations 
  are so confined anyways, I think this would just add noise.

- By keeping all of the adenylate conformations identical---even if that 
  conformation isn't perfectly ideal---rosetta will only be able to compare the 
  NCAA conformations, which is all I want it do do.

If I wanted to vary the adenylate coordinates, I thought of two reasonable ways 
to do so:

- Use B-factors from crystal structure.

- Use adenylates from aligned homologs.

How to pick which specific adenylate coordinates to use:

- I obviously need different coordinates for the class I and class II enzymes.

- M. mazei PylRS:

  - Most structures have ligand.

  - The following structures have an adenylated ligand (as opposed to ATP/AMP):

    .. datatable:: mma_pylrs_ligands.xlsx

      The best source is based purely on :math:`R_{free}`.

  - Probably I should try to find a structure with the Pyl-adenylate.  Since 
    that's the native substrate, it should be the most relaxed conformation.

  - I think 2zim-REDO has the best adenylate structure:

    - 2q7h and 2zim are the only structures of PylRS + Pyl-AMP.

    - These two structures are actually just different refinements of the same 
      data.  Both are also present in PDB-REDO, for a total of 4 refinements of 
      the same data.

    - The PDB-REDO models seem to be substantially better than the original PDB 
      ones.

    - 2q7h-REDO and 2zim-REDO are very similar to each other.  Given that 
      they're based on identical data, this isn't surprising.  If anything, 
      it's surprising that they differ at all, but presumably the refinement 
      process isn't deterministic.  Of the two, though, 2zim-REDO scores 
      slightly better in several metrics (:math:`R_free`, Ramachandran 
      outliers, fine packing, H-bond satisfaction) and worse in none.

  - If I'm going to use the adenylate coordinates from 2zim-REDO, I should also 
    use its protein coordinates for the design scaffold.

  - In all of these structures, the adenylates have almost identical structures 
    up to the phosphate.  In SMARTS::

      POC[C@H]3O[C@@H](n2cnc1c(ncnc12)N)[C@H](O)[C@@H]3O

    2021/12/21:

    Thinking about this more, I think it would be wise to include the Cα in the 
    anchor.  There's one structure that has a radically different Cα position 
    than the others: 3vqx.  The authors acknowledge the unnusual conformation, 
    and I'm not sure if there's any reason to think it represents the 
    transition state.  RDKit also does not generate a lot of structures with 
    the right Cα position on it's own.


- M. jannaschii TyrRS: 

  - See :expt:`10`

  - There are no MjTyrRS structures with the adenylate.

  - The only MjTyrRS structure with adenosine is 5n5u:

    - 5n5u has AMP and Tyr.
    - 5n5u is a structure of a engineered MjTyrRS mutant, so I don't want to 
      use its protein coordinates.
    - My plan is to use the protein coordinates from one of the wildtype 
      structures (maybe 1j1u) and the adenosine coordinates from 5n5u.

