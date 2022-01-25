********************************
MmPylRS PDB REDO stereochemistry
********************************

The 2zim model in PDB redo has at least two stereochemical errors relative to 
the 2zim model from the PDB.  I confirmed both by hand:

- 3' ribose hydroxyl: According to wikipedia, D-ribose should have both the 2' 
  and 3' hydroxyls on the same face of the ring.  This is the case for my 
  generated conformers and the PDB model, but not the PDB-REDO model.

- Cα: According to wikipedia, the L-serine amide should point towards the 
  viewer when the COOH and side chain are in plane, with the COOH on the 
  right and the sidechain on the left.  This is the case for my generated 
  conformers and the PDB model, but not the PDB-REDO model.

Some other observations:

- The "refined-only" PDB-REDO structures are almost planar at these chiral 
  centers; basically half-way between flipped and not.

- I think the PDB-REDO model has a bad sugar pucker as well.  This is based on 
  the observation that RDKit seemed resistant to making the pucker in the 
  PDB-REDO model, even when heavily constrained.  In contrast, RDKit seemed to 
  gravitate towards the pucker in the PDB model.

With this in mind, I should not use the PDB REDO models.

..update:: 2022/01/03

  I emailed the maintainers of PDB REDO about this error, and they fixed the 
  problem.  Here's the response:

    2zim was redone a while ago with a clearly wrong restraint file from the 
    CCP4 dictionary, thanks for pointing that out. The restraint file was 
    recently replaced in CCP4 so I reran 2zim (and 2q7h is also running). This 
    solved the chirality errors that were previously introduced, but not the 
    one already in the model at atom CBF (which therefore hides the interaction 
    with Trp 417).

    Annoyingly, the modelled chirality is consistent with the PDB definition of 
    YLY. So to fix this properly, the definition of YLY must be changed at the 
    side of the PDB. This only affects 2q7h and 2zim (both obviously wrong) so 
    this can probably be arranged. If you contact the PDB annotators, I'm happy 
    to back you up in solving this for good.

    Best wishes,
    Robbie Joosten

  I confirmed that the most recent PDB REDO entries have the correct 
  stereochemistry for this ligand.  The CBF atoms that Robbie mentions is the 
  methyl group attached to the pyrroline ring at the end of pyrrolysine.  To be 
  honest, I'm not sure what the chirality of that atom *should* be.  This isn't 
  really important, but I was interested so I looked into it more closely.

  There are a number of discrepencies between pyrrolysine and the PDB YLY 
  ligand:

  - I got a SMILES string for pyrrolysine from wikipedia::

      C[C@@H]1CC=N[C@H]1C(=O)NCCCC[C@@H](C(=O)O)N

  - This structure matches the structure and chirality associated with the CAS 
    database: https://commonchemistry.cas.org/detail?cas_rn=448235-52-7
  
  - The SMILES and InChI strings for YLY give different tautomers for the 
    internal amide.

    - SMILES: amide
    - InChI: imidic acid

    I have no idea how readily these two forms interconvert.

  - The 2D structure shown of the PDB ligand page matches the SMILES string 
    (and the wikipedia/CAS pyrrolysine structure).

  - Neither YLY string contains a double bond in the pyrroline ring, which 
    should be there according to CAS.

  - Both YLY strings have a different chirality than the wikipedia/CAS 
    structures at the pyrroline carbon that attaches to amide (CBK in the PDB 
    model).
    

