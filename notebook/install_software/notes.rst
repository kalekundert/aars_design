****************
Install software
****************

I want to make the pipeline that I'll ultimately create for this project as 
easy as possible for other people to use.  That means embracing modern 
containerization/distributed execution frameworks, which I don't know much 
about.  In particular, I expect the following frameworks to be relevant:

- Docker
- Conda
- NextFlow

Nextflow
========
Below I describe the conceptual pipelines that make up the design task.  I'm 
not sure whether they should be implemented separately, or as parts of a bigger 
pipeline.

Having browsed the NextFlow docs, I get the impression that it's meant to 
execute every process on every invocation: it's not really meant to evaluate 
what already been done, and to only do what hasn't.  It also doesn't seem to 
have a way to only execute a subset of the processes.  This suggests that it 
might be better to create separate pipelines for each conceptual task.

UPDATE: DSL2 adds the ability to define multiple workflows in a single NextFlow 
file, and to control the entry point.  It still requires the ``-resume`` option 
to skip processes it's already completed, but with this is mind, I think it'll 
be cleanest to have everything in one NextFlow file.  I get the impression that 
there will be some shared processes/configuration settings that will be easier 
to share this way.

I'll tell NextFlow that a conda environment with pyrosetta is required.  It'll 
then be on the user to (i) install conda and (ii) add the pyrosetta channel.  
That's not too onerous.  I think that's about as good as I can do without being 
able to distribute rosetta.

I'll also have to tell NextFlow to install my "ncaars" package in the conda 
environment.  This is a little trickier, but can be done using the "pip" flag 
of "environment.yml"::

  dependencies:
    - pyrosetta
    - rdkit
    - pip:
      - ./ncaars

.. update:: 2022/01/25

  I didn't end up trying the above idea, because even if it worked (which I 
  think it would), NextFlow would only install the ncaars package the first 
  time it runs, and would ignore any changes to it made afterward.

  The proper way to do this (I learned from looking at other NextFlow 
  pipelines) is to put the python scripts in the ``bin`` directory.  NextFlow 
  will automatically add this directory to ``$PATH`` in all processes.  It's 
  not compatible with distributing the code as a stand-alone python package, 
  but it's better to think of this as a NextFlow application rather than a 
  python application.

The NextFlow docs also recommend specifying the "conda" directive in a profile, 
so that it could be swapped out for other forms of containerization.  Although 
this approach makes more sense when there are out-of-the-box containers 
available.  I need something pretty bespoke.

Design
------
This pipeline will predict sequences to bind a given NCAA.

Required inputs:

- aaRS scaffold
- NCAA parameter file

Optional inputs:

- Hints about how many sequences to return.
- Which design algorithm to use.

Actions:

- Design:

  - Coupled moves
  - HBNet
  - EnzDes
  - GreedyOpt

Outputs:

- Design models: as mmCIF, PDB
- Design sequences: as FASTA
- Pymol sessions: e.g. for use with wt_vs_mut

Prepare scaffold
----------------
This pipeline will prepare a new aaRS scaffold for the design pipeline.

Required inputs:

- aaRS structure (with adenylate): e.g. downloaded directly from the PDB
- adenylate residue ID
- SMARTS string identifying the adenylate atoms to hold constant

Actions:

- Relax ≈50x with B-factor-derived restraints

Outputs:

- aaRS scaffold: a directory containing:

  - best-scoring relaxed model
  - adenylate residue ID
  - adenylate SMARTS string

Prepare ligand
--------------
This pipeline will prepare a new NCAA for the design pipeline.  I'm not totally 
sure if this should be it's own pipeline, or just a step in the first pipeline.

Required inputs:

- Amino acid: as SMILES, InChI, SDF, etc.
- aaRS scaffold

Actions:

- Create ligand conformations, e.g. RDKit
- Create Rosetta parameter file

Outputs:

- NCAA parameter file

Alternatively, if a parameter file was directly specified by the user, it will 
be passed through this process unchanged.


Docker
======
Because rosetta is closed source, I can't actually provide a docker container 
pre-configured to run the whole pipeline.  The best I can do is provide a 
Dockerfile and clear instructions for how the user can create the container 
themselves.

I still think it'll be worth using containers, though.  Without it, the 
installation instructions will be different for every HPC environment.  In 
other words, without a container, NextFlow will have to run commands directly 
on the host machines.  That means that the user will be responsible for 
installing any dependencies on each host machine.  I'll probably be able to fit 
all the dependencies as a single conda package (e.g. an "aars" package that 
itself depends on whatever I need), but that will still require users to figure 
out how to install conda and properly setup an environment on their system.  
Easier to have a single docker command that takes care of everything for every 
system.  Plus, maybe at some point there will be rosetta docker containers that 
I can just use.

UPDATE: The above isn't a true concern; nextflow has the built-in ability to 
create a conda environment for each process.

Also, it might have things like fragment databases that could be stored in the 
container.

I'm not sure if I'll need docker or not.

Conda
=====
Conda is a package manager.  I think of it as a peer to pacman, dnf, apt, etc.  
The main difference in my mind is that conda seems to have more scientific 
software, including Rosetta and RDKit.  (Although now that I think about it, 
conda may also be better suited for maintaining multiple different 
environments).
