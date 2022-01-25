*****************
Design algorithms
*****************

The goal of this project is to create an algorithm that can be used to design 
aaRSs for any NCAA, and to convincingly show that the algorithm works.  I have 
only been able to find 2 examples of Rosetta being used to design aaRSs, and 
neither is directly suitable for for this task:

[Hauf2017]_, [Baumann2019]_:

- Based on enzyme design.
- Matching stage requires that specific interactions with the NCAA be 
  specified.  This would be hard to do in a general way.

[Beyer2020]_:

- Based on GreedyOpt
- GreedyOpt is meant to be used as a proxy for "human intuition" *after* a 
  design run.
- [Beyer2020]_ skipped the actual design run step, because they already had a 
  crystal structure of the aaRS binding their ligand (from a previous directed 
  evolution screen).  So there isn't really any reason to expect that this 
  would be a good approach for designing a *new* aaRS, but I suppose its still 
  worth trying.

Some features that I think the algorithm will need to have:

- Anchor the NCAA via the adenylate.

  - The conformation of the adenylate is very conserved.
  - Doesn't depend on any atoms in the NCAA itself.

- Backbone flexibility:

  - fKIC for MjTyrRS
  - backrub/coupledmoves/minimization for MmPylRS

- NCAA H-bonds:

  - Important for specificity
  - Can try accounting for with:

    - HB-Net
    - some buried unsat score term


  
