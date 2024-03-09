from rdkit import Chem
from rdkit.Chem import inchi

def standardise_inchikey(smiles_list):
    inchikey_list = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            inchikey = inchi.MolToInchiKey(mol)
            inchikey_list.append(inchikey)
        else:
            inchikey_list.append(None)
    return inchikey_list