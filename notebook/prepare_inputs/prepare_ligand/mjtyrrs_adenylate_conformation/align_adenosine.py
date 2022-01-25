#!/usr/bin/env python3

import pandas as pd
import nestedtext as nt
import subprocess

from rdkit.Chem import AllChem as Chem, Draw
from pprint import pprint
from dataclasses import dataclass
from more_itertools import one
from pathlib import Path

anchor_key = 'ribose'

ROOT_DIR = Path(__file__).parent 
INPUT_DIR = ROOT_DIR / 'homologs'
OUTPUT_DIR = ROOT_DIR / f'homolog_ligands_aligned_to_{anchor_key}'
CONFIG_PATH = ROOT_DIR / 'homolog_ligands.xlsx'

@dataclass(frozen=True)
class ResiduePath:
    model: str
    segment: str
    chain: str
    resn: str
    resi: int

    @classmethod
    def from_str(cls, path_str):
        fields = path_str.split('/')
        if fields[0] != '':
            raise ValueError("expected absolute path, not: {path_str!r}")

        fields = fields[1:]
        fields[4] = int(fields[4])

        return cls(*fields)

df = pd.read_excel(CONFIG_PATH)

mols = {}

# These anchors are carefully written to accommodate the 7AP3 ligand, which is 
# an adenosine analog.
anchor_smarts = {
        'adenine': 'c1c2ncnc2*c*1',
        'adenosine5': 'n2c1c(*c*c1n(c2)[C@@H]3O[C@@H]([C@@H](O)[C@H]3O)CO)',
        'adenosine4': 'n2c1c(*c*c1n(c2)[C@@H]3O[C@@H]([C@@H](O)[C@H]3O))',
        'amp': '*OC[C@H]3O[C@@H](n2cnc1c(*c*c12))[C@H](O)[C@@H]3O',
        'ribose': 'OC[C@H]3O[C@@H][C@H](O)[C@@H]3O',
}
anchor = Chem.MolFromSmarts(anchor_smarts[anchor_key])

bond_order_templates = {
        k: Chem.MolFromInchi(v)
        for k, v in nt.load(ROOT_DIR / 'bond_order_templates.nt').items()
}

groups = {}

def add_to_group(model, group, value):
    # Nested dicts to order the groups nicely.
    groups.setdefault(group, {}).setdefault(value, []).append(model)

# Load ligands:

for i, row in df.iterrows():
    res = ResiduePath.from_str(row['Adenosine path'])
    pdb_path = one(INPUT_DIR.glob(f'{res.model}_*.pdb'))
    mol = Chem.MolFromPDBFile(str(pdb_path))

    # This model breaks things because the ligand is entered as if it were two 
    # molecules.
    if res.model == '3vgj':
        continue

    # The PDB format lacks bond-order information, and we have to add it back 
    # in for the alignment to work:
    template = bond_order_templates[res.resn]
    mol = Chem.AssignBondOrdersFromTemplate(template, mol)

    mols[res.model] = mol

    add_to_group(res.model, 'species', row['Species'])
    add_to_group(res.model, 'amino acid', row['Amino Acid'])
    add_to_group(res.model, 'adenylate', res.resn)

# Align ligands:

probe_mols = mols.copy()
ref_mol = probe_mols.pop('5n5u')
ref_atom_ids = ref_mol.GetSubstructMatch(anchor)

for key, probe_mol in probe_mols.items():
    probe_atom_ids = probe_mol.GetSubstructMatch(anchor)

    if not probe_atom_ids:
        raise ValueError(f"{key} does not contain {anchor_key!r}")

    atom_map = list(zip(probe_atom_ids, ref_atom_ids))
    rmsd = Chem.AlignMol(probe_mol, ref_mol, atomMap=atom_map)

# Output SDF files:

OUTPUT_DIR.mkdir(exist_ok=True)
sdf_paths = []

for key, mol in mols.items():
    sdf_path = OUTPUT_DIR / f'{key}.sdf'
    sdf_paths.append(str(sdf_path))
    with Chem.SDWriter(str(sdf_path)) as w:
        w.write(mol)

# Output pymol session:

pml_path = OUTPUT_DIR / 'load.pml'
pse_path = OUTPUT_DIR / f'alignment.pse'

pymol_script = []
for k in groups:
    for group, models in groups[k].items():
        pymol_script.append(f"select {group}, {' or '.join(models)}")
pymol_script.append("as lines")
pymol_script.append("util.cbag")
pymol_script.append(f"save {pse_path}")

with open(pml_path, 'w') as f:
    f.write('\n'.join(pymol_script))

subprocess.run(['pymol', '-c', *sdf_paths, '-u', str(pml_path)])



