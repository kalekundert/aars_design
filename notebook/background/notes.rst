**********
Background
**********

Notable Structures
==================
Below are the structures that I've most carefully studied and annotated, and/or 
where the global architecture is well described by the accompanying reference.

1A8H:

- [Sugiura2000]_
- T. thermophilus MetRS
- Class Ia
- 2.0Å
- Normally dimeric (unusual for class Ia aaRS), but this structure is without 
  the dimerization domain.  The enzyme retains near full activity in its 
  monomeric form [Sugiura2000]_.
- Single CP domain, not divided into CP1/CP2

1SET/1SER:

- T. thermophilus SerAS
- Class IIa

1QF6:

- [Sankaranarayanan1999]_
- E. coli ThrRS
- Class IIa

Structures
==========
1SES:

- T. thermophilus SerAS
- Class II
- Can't find motif 3: gxgxgf[de]R

1ASY:

- S. cerevisiae AspRS:tRNA complex
- class II

1P7P:

- E. coli MetRS
- Class I?

1h3n:

- [Cusack2000]_
- T. thermophilus LeuRS
- Class Ia
- 2.0Å

4aq7:

- E. coli LeuRS
- Class Ia
- Compared to T. thermophilus MetRS:

  - Bigger CP domain; includes editing functionality
  - Extra C-terminal domain

1gsg:

- E. coli GlnRS:tRNA
- Cα only!

1gln:

- T. thermophilus GluRS
- Class Ib

1n77:

- T. thermophilus GluRS:tRNA
- Note that GluRS requires tRNA to adenylate Glu.  Without tRNA, the ATP 
  molecule binds in an inactive pocket. [Sekine2003]_


Classes
=======

Overview
--------
From Table 1 in [Geige2016]_:

- Class Ia: Leu, Ile, Val, Arg, Cys, Met
- Class Ib: Glu, Gln
- Class Ic: Tyr, Trp

- Class IIa: Ser, Thr, Pro, His, Gly
- Class IIb: Asp, Asn, Lys
- Class IIc: Ala, Phe


Class I
-------
Distinctive features:

- ATP-binding domain: Rossman fold [Geige2016]_

- Mostly monomeric [Geige2016]_

- Mostly charge large nonpolar/aromatic amino acids

- Bind the acceptor stem in the minor groove [Geige2016]_.

- Amino acid attached to 2'-OH [Geige2016]_.

  - The amino acid must be moved to the 3'-OH before it can be used by the 
    ribosome.  It's not immediately clear to me if this isomerization is 
    catalyzed by some other factor, or if it occurs spontaneously.

- Motifs: [Geige2016]_

  - Binding/interacting with ATP:

    - HiGh
    - kmSKs

Class II
--------

Distinctive features:

- ATP-binding/catalytic domain:

  - 7-stranded anti-parallel β-sheet [Geige2016]_
  - Back face of β-sheet forms the dimer interface [Sankaranarayanan1999]_

- Mostly dimeric [Geige2016]_

- Mostly charge small, polar amino acids

- Bind the acceptor stem in the minor groove [Geige2016]_.

- Amino acid attached to 3'-OH [Geige2016]_.

- Motifs: [Geige2016]_

  - Dimerization:

    - motif 1: gΦxxΦxxP

  - Binding/interacting with ATP:

    - motif 2: fRxe

      - Located on a loop between 2 strands on the β-sheet. [Belrhali1994]_
      - This loop may also help bind the acceptor end of the tRNA. 
        [Belrhali1994]_
      - The presence of the adenylate may help position this loop to bind the 
        tRNA. [Belrhali1994]_
      - The strictly conserved R interacts with the α-phosphate of ATP/AMP 
        [Belrhali1994]_
      - The E forms H-bonds with the adenosine base. [Belrhali1994]_

    - motif 3: gxgxgf[de]R

      - β-strand adjacent to the strands flanking motif 2 [Belrhali1994]_
      - The "gxgxg" motif makes up the face of the β-strand facing towards the 
        ATP.  The glycines (or other small amino acids) are probably required 
        to avoid filling the space that should be occupied by the sugar/base of 
        ATP.
    
  - "The high degeneracy of the three motifs in class II aaRSs has to be 
    noticed.  With only one proline and two arginine residues strictly 
    conserved, these signatures could not be discovered on a sole sequence 
    inspection but required knowledge of 3D structures in which the 
    single-signature amino acids are similarly located in specific 
    architectural frameworks." [Geige2016]_


Class Ia
--------
Distinctive features:

- Mostly monomeric

- Charge hydrophobic amino acids [Geige2016]_

- Connective polypeptide (CP) domain:

  - Insertion within Rossman-fold catalytic domain [Sugiura2000]_
  - 4-stranded anti-parallel β-sheet [Sugiura2000]_
  - Similar to class Ib ACB domain, very different from class Ic [Sugiura2000]_
  - The CP domain may surround one of the β-sheets from the Rossman fold, in 
    which case the two halves of the CP domain are referred to as CP1 and CP2.
  - The CP domain has editing functionality (except for MetRS).

- Stem contact (SC) domain:

  - Contacts the conserved G10-C25 base pair in the anticodon stem of the tRNA.  
    [Sugiura2000]_
  - Contains KMSKS motif, which is part of the active site that binds 
    adenosine.
  - The KMSKS loop conformation changes upon tRNA binding.

    - This change might also relate to the fact that the same active site is 
      used for aminoacyl-AMP and aminoacyl-tRNA formation.

- Anticodon-binding (ACB) domain:

  - α-helical bundle [Geige2016]_
  - defining feature of class Ia

Members:

- MetRS, CysRS:

  - CP domain is either short or absent and has no editing functionality.
    This make sense, because Cys/Met are more unique than Ile/Leu/Val.

- IleRS, LeuRS, ValRS:

  - CP1 domain is large and has editing functionality.
  - The need for an editing domain makes sense, because Ile/Leu/Val are hard 
    to distinguish.

- LeuRS:

  - 50 aa insertion prior to KMSKS loop.
    
    - If I understand correctly, this insertion is involved with tRNA 
      binding.  [Geige2016]_ [Tukalo2005]_ [Cusack2000]_
    - Required for aminoacylation, not for editing [Geige2016]_ [Cusack2000]_

  - α/β C-terminal RNA-binding domain, after the ACB.

    - Only visible in LeuRS:tRNA structures.

- ArgRS

  - "Add1 and Add2 (Additional domains) are the two nucleic acid-binding 
    modules attached at the N- and C-terminal sides of the catalytic domain." 
    [Geige2016]_
  
  - "Ins-1 and Ins-2 (Insertion domains) are inserted modules in the first 
    and second half of the Rossmann fold (RF1 and RF2)." [Geige2016]_

  - Add1:

    - Shares topology with ribosome release factor
    - Recognizes D-stem and loop of tRNA.

  - Add2 is the same as ACB in other class Ia aaRS enzymes

  - Requires cognate tRNA to amino acid activation (e.g. to form 
    arginyl-AMP).

    - This behavior is unusual, and characteristic of class Ib aaRS enzymes.

Class Ib
--------
Distinctive features:

- Monomeric

- Can only catalyze amino acid activation when tRNA is bound.
  
  - "For these synthetases, the tRNA serves as the activator in the first 
    step, and as the substrate in the second step of aminoacylation." 
    [Sekine2003]_

- Acceptor-stem binding (ABD) domain:

  - Analogous to CP domain from class Ia.
  - Not sure whether or not it has editing functionality.

- Anticodon binding (ACB) domains:

  - Two domains, as compared to 1 in class Ia.
  - Topology isn't conserved.

- Extant GlnRS enzymes likely arose from non-discriminating GluRS enzymes.

Members:

- GluRS:

  - ACB domains: α-helical (but not a bundle) [Geige2016]_
  - Often non-discriminatory: meaning that it will charge Glu onto the Glu or 
    Gln tRNA.  In species with non-discriminatory GluRS enzymes, there will 
    be another enzyme that converts Glu to Gln on mischarged tRNAs.

- GlnRS:

  - ACB domains: β-barrel [Geige2016]_

- LysRS-I:

  - Most bacterial species have class IIb LysRS enzymes.
  - However, a few species have class Ib LysRS enzymes that derive from 
    archaea and have very similar architecture to GluRS/GlnRS.

Class Ic
--------
Distinctive features:

- Obligate dimers, where each tRNA binds one monomer and sits in the active 
  site of the other [Geige2016]_ [Sugiura2000]_.

- Connective polypeptide (CP) domain:

  - "Counterclockwise-arranged α helices that form a dimer interface"  
    [Sugiura2000]_
  - Very different from class Iab CP domains: smaller and no editing 
    functionality [Geige2016]_

Members:

- TyrRS

  - Two C-terminal domains for binding tRNA:
      
    - α-ACB: α-helical bundle that binds the anticodon
    - S4: homologous to ribosomal protein S4, required to bind long variable 
      stem of tRNA, not present in archaeal or eukaryotic TyrRS.

- TrpRS

  - Smallest aaRS enzymes (328 aa for B. stearothermophilus).
  - Unique C-terminal ACB domain.

Class IIa
---------
Distinctive features:

- Charge small and polar amino acids [Geige2016]_

- Anticodon binding (ACB) domain:

  - C-terminal α/β architecture

- Overall a heterogeneous group of enzymes, with many idiosyncratic 
  insertions/domains.

Members:

- SerRS, ThrRS, ProRS:

  - Closely related
  - "Interestingly, the structural relatedness concerns also the three amino 
    acids, with serine and threonine capable of forming an internal H-bonded 
    five-membered ring structure that mimics the ring structure of proline" 
    [Geige2016]_

- ThrRS, ProRS:

  - Only class IIa enzymes with editing domains.

- SerRS:

  - Unique N-terminal coiled-coil ACB domain that stretches 60Å into solvent in 
    the apo state.  When tRNA is bound this domain interacts extensively with 
    its anticodon, variable, and T arms.  The tRNA bound by this domain sits in 
    the active site of the other monomer.

  - Lacks distinctive class IIa ACB, but included in this class due to clear 
    structural and phylogenetic relatedness.

  - Does not recognize anticodon.

- ThrRS:

  - "In E. coli, the biosynthesis of ThrRS is autoregulated by a feedback 
    mechanism at the translational level (45). The enzyme binds to the leader 
    of its own mRNA close to the translation initiation site, thereby 
    inhibiting ribosome attachment and thus translation (33). The issue of 
    whether the mRNA recognition is equivalent to that of tRNA-Thr has been the 
    object of intensive study, and the current model predicts that the 
    messenger contains two RNA stem loops that mimic the tRNA anticodon arm 
    (24, 40)." [Sankaranarayanan1999]_

  - N-terminal editing domains:

    - Divided into 2 parts: N1 and N2 [Sankaranarayanan1999]_

    - N1:

      - ≈50 aa N-terminal domain.
      - α/β topology from ubiquitin family. [Sankaranarayanan1999]_

    - N2:

      - Wraps around the acceptor stem (the active site binds the other side of 
        the stem). [Sankaranarayanan1999]_

      - "It is known that the first two base pairs of E. coli tRNAThr are 
        important identity determinants." [Sankaranarayanan1999]_.  It is likely 
        that this domain contributes to this specificity.

      - Responsible for hydrolyzing mischarged seryl-tRNA(Thr) 
        [Sankaranarayanan1999]_

  - Zn in active site [Sankaranarayanan1999]_.

    - Only 3 residues chelate the Zn atom, leaving one space open and 
      indicating that the Zn probably plays a role in catalysis 
      [Sankaranarayanan1999]_.

    - MetRS and IleRS also contain Zn, but not in the active site.

- ProRS:

  - 2 evolutionary groups: bacterial and archaeal/eukaryal.

    - The E. coli enzyme is in the archaeal/eukaryal group [Geige2016]_.

    - archaeal/eukaryal group: Zn-binding domain after class IIa-specific ACB 
      domain. [Geige2016]_.

    - bacterial group: ≈180 aa editing domain inserted into the catalytic 
      domain.

- HisRS:

  - ≈60 aa helical insertion in the catalytic domain between motifs 2 and 3.  
    [Geige2016]_.  This insertion is mobile and likely contacts the tRNA 
    acceptor stem.

  - ACB domain that resembles part of a β-barrel (i.e. different from ThrRS, 
    but still α/β) [Geige2016]_.

- GlyRS:

  - Two distinct kinds of GlyRS: α₂ dimer and α₂β₂ tetramer [Geige2016]_.

    - E. coli: α₂β₂ tetramer [Geige2016]_
    - No structures of the α₂β₂ tetramer are available yet [Geige2016]_

  - α₂ dimer:

    - Insertion in catalytic domain that likely interacts with the tRNA 
      acceptor stem [Geige2016]_.
    - ACB domain: unique α/β architecture [Geige2016]_.

Class IIb
---------
Distinctive features:

- Homodimeric
- Charge polar amino acids [Geige2016]_

- Anticodon-binding (ACB) domain:

  - "OB-folds (40) a common motif with β-barrel architecture found in many 
    proteins (218)" [Geige2016]_.

  - Note that Lys, Asp, and Asn have very similar anticodons, particularly in 
    the two 3' positions:

    - Lys: UUU, CUU
    - Asp: GUC, AUC
    - Asn: GUU, AUU

Members:

- AspRS

  - GatB/aaRS (GAD) domain:
    
    - 5-stranded anti-parallel β-sheet flanked by 3 α-helices [Geige2016]_.
    - Inserted between motifs 2 and 3 in the catalytic domain [Geige2016]_.
    - Strong homology to archaeal GatB protein, which catalyzes a 
      transamidation reaction.  This suggests that the GAD domain has a role in 
      non-discriminatory Asn charging. [Geige2016]_.

- AsnRS:

  - Very similar to AspRS, but lacks GAD domain (see above).

- LysRS:

  - Two forms:

    - LysS: constitutive
    - LysU: expressed in response to heat shock; maybe due to moonlighting 
      ability to synthesize "alarmones" [Geige2016]_.
    - 88% sequence identity between the two forms [Geige2016]_.

  - Mg²⁺ coordinating ATP and lysine in active site [Geige2016]_.

Class IIc
---------
Distinctive features:

- Tetrameric
- Have editing ability

Members:

- AlaRS:

  - "Interestingly, among aaRSs, AlaRSs have the highest degree of sequence 
    conservation and have limited similarity with other aaRSs (18)." 
    [Geige2016]_.

  - Four domains (from N to C):

    - Catalytic domain
    - tRNA recognition domain
    - editing domain
    - oligomerization domain

- PheRS:

  - (αβ)₂ dimer-of-dimers architecture:

    - α-subunit, 3 domains:

      - A1,A2: class-distinctive antiparallel β-sheet active site.
      - A0: helical RNA binding domain that interacts with tRNA in opposite 
        active site.

    - β-subunit, 8 domains:

      - B1,B5: Interact with α-subunit.
      - B2: OB-fold domain, reminiscent of class IIb.  Doesn't seem to be 
        involved in anticodon recognition, though.
      - B3,B4: editing domain
      - B6,B7: "cryptic “catalytic-like” domain without class II signatures" 
        [Geige2016]_
      - B8: anticodon binding

  - "Remarkably, comparison of the T. thermophilus PheRS structure with the E. 
    coli PheRS structure uncovers significant rearrangements of the structural 
    domains involved in tRNAPhe binding/translocation (234)." [Geige2016]_

  - Overall, I think it's fair to say that PheRS is a really complicated 
    enzyme, and that it probably participates in several regulatory pathways.

Catalysis
=========

Allostery
---------
- "The fact that aaRSs are multidomain proteins implies the existence of 
  communication between domains and of coupled domain motions. In other words, 
  functional aaRS:tRNA complexes can be considered as “signal transduction” 
  systems in which specific conformational changes occur, which can be subtle 
  or dramatic (264, 350, 351)." [Geige2016]_.

Error Correction
================
Three processes responsible for fidelity [Geige2016]_:

- tRNA aminoacylation
- Selection of aminoacylated tRNAs by EF-Tu
- Decoding of mRNA by tRNA anticodons

tRNA aminoacylation
-------------------
See Table 5 in [Geige2016]_ for a list of the editing mechanisms for each aaRS.  
This will be good to consult once I figure out which aaRS we'll be designing.

- "Inaccuracy in amino acid selection (10−4 to 10−5) is more frequent than tRNA 
  selection (10−6) because of the larger surface area of the tRNA molecules and 
  the resulting greater structural diversity of the contact regions." 
  [Geige2016]_

Double-sieve mechanism [Geige2016]_:

- Not all aaRSs adhere to this mechanism, but many do and it's a useful 
  framework to have in mind.

- The aminoadenylation active site is the right size for the cognate amino 
  acid, and therefore sieves out any non-cognate amino acids that are too big.

- The editing active site is just a bit too small for the cognate amino acid, 
  and therefore sieves out any non-cognate amino acids that are too small.

- My guess is that thinking just about "size" is too simplistic: it's really 
  about chemical compatibility.  For example, the aminoadenylation site might 
  exclude smaller non-cognates via polar/H-bond interactions.  Likewise, the 
  editing site might exclude the cognate in the same manner, while still 
  physically having enough space for it.

Pre-transfer editing:

- This is basically editing that occurs in the synthesis active site, after the 
  amino acid is activated but before it is attached to tRNA.

- This functionality is assumed to have evolved before dedicated post-transfer 
  editing domains [Geige2016]_.

Post-transfer editing:

- Editing by devoted domains, distinct from the main active site, occurring 
  after the amino acid has been transferred to the tRNA.

- The nucleotide determinants for adenylation and editing activity can differ, 
  because (i) the active sites are different and (ii) the tRNA has to 
  move---coming into contact with different aaRS residues---to reach the 
  editing active site [Geige2016]_.  In principle, this means that you could 
  design a tRNA sequence to evade editing.

- Editing domains can usually be separated from the aaRS and retain function 
  [Geige2016]_.

Engineering
===========
- "Because of kingdom-specific distinctions in tRNA aminoacylation systems, 
  expression of alloproteins in E. coli cells essentially relies on engineered 
  aaRS/tRNA pairs of heterologous origin" [Geige2016]_
  
  - M. jannaschii: Tyr
  - S. cerevisiae: Asp, Gln, Tyr, Phe

- "Although several strategies to generate orthogonal aaRS/tRNA pairs have been 
  explored, ultimately, the most straightforward solution involves the 
  importation of a heterologous aaRS/tRNA pair from a different domain of 
  life."

Common tRNA/aaRS pairs:

- Methanocaldococcus jannaschii Tyr [Liu2010]_

  - Class Ic
  - No editing domain.
  - 36 crystal structures:

    - 1J1U:

      - seems like it might be a good starting point.
      - KMSKS motif not resolved, though.

- S. cerevisiae Asp

  - Class IIb

- S. cerevisiae Gln

  - Class Ib

- S. cerevisiae Tyr

  - Class Ic

- S. cerevisiae Phe

  - Class IIc

- Methanosarcina barkeri Pyl

  - Class IIc
  - No crystal structures.

- Methanosarcina mazei Pyl

  - Class IIc
  - Lots of high-resolution crystal structures with various Pyl derivatives, 
    although none with tRNA.

- Desulfitobacterium hafniense Pyl

  - Class IIc
  - 2 crystal structures:

    - 2ZNJ: 2.5Å
    - 2ZNI: 3.1Å, includes tRNA

