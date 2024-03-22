> _This README file contains the information about the datasets contained in the `data` directory._

# Task-1:

- `raw_data.tsv` : The dataset was downloaded from ChEMBL in tsv format. Dataset contains 8715 entries having dimensions named Smiles, InchiKey among others.
- `input_data.csv` : This dataset contains 1000 entries sampled from raw_data after preprocessing.
- `output_data.csv` : The predictions made by the model after running on input_data.csv were saved in this csv file.

# Task-2:

- `Table S6.xslx` : This is the dataset used by the authors as mentioned in the publication. The dataset was provided as a Supporting Information by the authors and was downloaded from the GitHub repository of the model created by the authors.
- `input_task2.csv` : This dataset was created as an input file for the model to run predictions on, after extracting Smiles and InchiKey columns from the Table S6.xslx
- `output_task2.csv` :  The predictions made by the model after running on input_task2.csv were saved in this csv file.

# Task-3:

- `external_dataset.csv` : The dataset contains 1092 records in which 234 records are hERG blockers and the rest are non-blockers. This dataset was used by Li et al in their publication "Modeling of the hERG K+ Channel Blockage Using Online Chemical Database and Modeling Environment (OCHEM)"
- `trainingset.sdf` : This dataset was used by the authors to train the deepherg model.
- `trainingset.csv` : The trainingset.sdf file was converted to csv format and saved as trainingset.csv
- `input_task3.csv` : This dataset contains the molecules after eliminating repeated molecules between train and external dataset.
- `output_task3.json` : The predictions made by the model after running on input_task3.csv were saved in this json file.
- `output_task3.csv` : The output_task3.json file was converted to csv file and saved as output_task3.csv

