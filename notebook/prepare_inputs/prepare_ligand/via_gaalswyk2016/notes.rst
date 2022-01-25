*******************
Via [Gaalswyk2016]_
*******************

The conformer generation literature generally seems to acknowledge that MD is 
the most accurate method, albeit far too expensive for the usual applications 
(e.g. docking).  That said, this was to only reference I could find that 
actually used MD to generate conformations.  I'm a little hesitant to use it 
though, because I haven't seen it in any third-party comparisons.

- [Gaalswyk2016]_ uses NAMD.  The option for holding atoms fixed in NAMD is 
  described here:

    https://www.ks.uiuc.edu/Research/namd/2.9/ug/node27.html

  Looks like I'll have to munge the PDB input, though.  Ugh.

- The clustering algorithm is the one implemented by the ``measure cluster`` 
  VMD command.  It's called "quality threshold clustering", and I like the 
  idea.  Basically: find all pairwise distances, make cluster from point with 
  most neighbors within some distance, remove all those points, repeat.  
  Probability is really a reflection of energy in these simulations, so we do 
  want the biggest clusters.

I'm really turned off by the quality of the code.  Very fragile.  I'll have to 
rewrite a lot myself, although hopefully I can use most of the config files as 
is.
