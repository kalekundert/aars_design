***************
Via RDKit/ETKDG
***************

Here I'm going to experiment with using RDKit to generate adenylated NCAA 
conformers.

- [Ebejer2012]_ claims that RDKit and confab are the best two open-source 
  conformer generation methods.  However, note that this is a pre-ETKDG version 
  of RDKit, which the RDKit documentation itself recommends against using for 
  anything other than quick visualization.

- [Friedrich2017]_ claims that RDKit is the best open-source conformer 
  generation method.  Both the DG (i.e. default before 2016) and ETKDG (i.e.  
  default after 2016) algorithms are copmared, and are found to perform 
  identically.

- It seems that RDkit may not do a good job making sugar puckers, even with the 
  version 3 small ring torsions enabled.

- The warning message "More than one matching pattern found - picking one" is 
  generated when assigning bond orders to the molecule loaded from the PDB.  
  The cause is that the two phosphate oxygens can't be distinguished, so it has 
  to pick an assignment arbitrarily.
  
  In reality, I don't think these two oxygens are actually different.  If 
  neither oxygen is protonated (net negative charge), they're equivalent by 
  resonance.  If one oxygen is protonated (net neutral charge), the proton 
  probably shuttles between the two very rapidly.  According to wikipedia, AMP 
  has 3 pKas: 0.9, 3.8, and 6.1.  Assuming that these refer to the 3 phosphate 
  protons, the proton is question would usually be absent at pH=7.

- RDkit does a very bad job actually satisfying the coord map.  The more atoms 
  it has to constrain, the worse it seems to do.

  - I could generate conformers until I find one that's close to the intended 
    coordinates, then swap in the desired coordinates, then minimize.  But then 
    I'd basically be rolling my own algorithm; no telling how good it is.

  - I could also maybe try generating my own distance matrix.  In particular, I 
    could either skip the smoothing step, or apply my "fixed" coords after 
    smoothing.  This might also not work very well.

    - See rdkit.Code/GraphMol/DistGeomHelpers/Embedder.cpp:869.  The coord map 
      is only applied before triangle smoothing.

    - This actually seems to work.  I need to add a ±0.1Å tolerance to the 
      "ideal" distance in order to get any conformers, but they're all pretty 
      well superimposed.

      - I still need to check the alignment, though.  When I generate ~100 
        conformers, I sometimes get some that significantly move the anchor 
        atoms.

    - These conformers are close enough that I'd feel comfortable removing all 
      variability in the aligned atoms by superimposing the last three atoms of 
      each conformer on the reference model, then copying the reference 
      coordinates over.

    - One problem I noticed is that I still generate conformers with the amino 
      acid pointing out of the active site.  I could use the bounds matrix to 
      eliminate these.  Some ideas:

      - Allow the scaffold to specify an ensemble of structures.  Any atoms 
        that match will be given distance bounds compatible with the whole 
        ensemble.  This is a little tricky, though, because after the backbone 
        there are no atoms guaranteed to be in all amino acids (and NCAAs may 
        not even have all the backbone atoms).

      - Allow some way to specify what the binding pocket is.  Maybe a SMARTS 
        query for the sidechain, or maybe a selection in the protein itself.  

      - This could also be a post-processing step; that might be more robust.

- When the random seed is set, `EmbedMultipleConfs` just makes the same 
  conformation every time.

- Clustering:

  - RDKit doesn't do any clustering by default.

  - It does have an RMS cutoff argument, but it doesn't work when constraining 
    coordinates.

  - But I don't think I need to cluster.  I'm not having problems where all of 
    my structures look similar.

- Pocket algorithm:

  - Goal: I want to encourage conformers that lie in the binding pocket.

  - Algorithm:

    - User specifies SMART string that identifies the binding pocket.

    - Find graph distance from each atom in the pocket to the closest anchor 
      atom.

    - Find physical distance from each atom in the pocket to each atom in the 
      anchor.  Save the smallest (and largest?) physical distance for each 
      graph distance.

    - For each non-anchor adenylated NCAA atom:

      - Find graph distance to the "closest anchor atom" from above.

      - Lookup the smallest and largest physical distances from each anchor 
        atom for that graph distance.

      - Apply those physical distances to the bounds matrix, maybe with a fudge 
        factor.
  
  - The nice thing about this algorithm is that the inputs are really simple: 
    Just a smarts string.

  - A similar idea could be applied as a post-generation filtering step, but 
    with the specific algorithm that RDKit has, it's much more efficient to do 
    it in advance.

