********************
Via Confab/OpenBabel
********************

According the [Ebejer2012]_, Confab performs as well as RDKit.

- Having read the command-line docs_, it' doesn't seem like there's any way to 
  used known coordinates for a subset of the atoms.

  But it seems like the C++ API, at least for the genetic algorithm, does 
  provide a way to do this.  In particular, see 
  ``ObConformerSearch::SetFixedBonds()``.

  http://openbabel.org/api/2.3/group__conformer.shtml

- Substructure matching (C++ API):

  http://openbabel.org/api/2.3/group__substructure.shtml 
  http://openbabel.org/api/2.3/classOpenBabel_1_1OBSmartsPattern.shtml

- Python API::

    from openbabel import openbabel
    openbabel.OBConformerSearch

.. _docs: https://open-babel.readthedocs.io/en/latest/3DStructureGen/multipleconformers.html

