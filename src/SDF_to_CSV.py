from rdkit import Chem
from rdkit.Chem.ChemUtils import SDFToCSV

# input file format: *.sdf
# output file format: *.csv

train_out = open('output_file/trainingset.csv', 'w')
train_in = Chem.SDMolSupplier('input_file/trainingset.sdf')
SDFToCSV.Convert(train_in, train_out, keyCol=None, stopAfter=- 1, includeChirality=False, smilesFrom='')
train_out.close()