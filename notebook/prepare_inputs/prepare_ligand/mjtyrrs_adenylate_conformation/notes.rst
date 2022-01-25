******************************
MjTyrRS adenylate conformation
******************************

Picking adenylate conformations is more complicated for MjTyrRS than for 
MmPylRS, because there aren't any structures of MjTyrRS binding the adenylate.  
In fact, the only MjTyrRS structure that has adenosine at all is :pdb:`5n5u`:

- :pdb:`5n5u` has AMP and Tyr.
- :pdb:`5n5u` is a structure of a engineered MjTyrRS mutant, so I don't want to 
  use its protein coordinates.
- My plan is to use the protein coordinates from one of the wildtype structures 
  (maybe :pdb:`1j1u`) and the adenosine coordinates from :pdb:`5n5u`.
- I want to use adenosine coordinates from an MjTyrRS structure (as opposed to 
  some homologous TyrRS) because I see in the case of MmPylRS structures that 
  the position of the adenylate is very well conserved.

I want to know how much the AMP phosphate moves when an amino acid is attached 
to it.  To figure this out, I aligned every TyrRS structure (and some TrpRS 
structures that got thought my filters) I could find.  The following have 
adenosine (in any form, e.g.  AMP, ATP, AA-adenylate):

.. datatable:: homolog_ligands.xlsx

I then took the adenylate ligand from each of these structures, and aligned the 
following moieties using rdkit.  I made different alignments for each of the 
following sets of atoms (accounting for the fact that some of the ligands are 
actually adenosine analogs):

- adenine
- adenosine
- adenosine (excluding the 5'C-OH)
- adenosine monophosphate

Observations:

- adenosine (excluding the 5'C-OH)

  - The eukaryotic structures position the tyrosine differently from most of 
    the prokaryotic/archaeal structures, but the sugar conformation doesn't 
    cluster by species.

  - The Trp structures all have ATP, and all position the PPi moiety 
    differently than the one Tyr structure with ATP.

- From looking at these structures, it seems like the torsion angle around the 
  (5'C)-(4'C) bond sometimes rotates nearly 180° when the AMP is adenylated.

