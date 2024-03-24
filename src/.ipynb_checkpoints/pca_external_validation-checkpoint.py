import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Define a function to calculate Morgan fingerprints
def calculate_morgan_fingerprints(smiles_list, radius=2, n_bits=2048):
    fingerprints = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
            fingerprints.append(fingerprint)
        else:
            fingerprints.append(None)
    return fingerprints

# Define a function to perform PCA
def perform_pca(fingerprints):
    # Convert fingerprints to numpy array
    fingerprint_array = np.array([np.frombuffer(fp.ToBitString().encode(), dtype=np.uint8) for fp in fingerprints if fp is not None])
    # Apply PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(fingerprint_array)
    return pca_result
