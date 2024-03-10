# Model: eos30gr - Deep hERG Blocker Classification

## Overview

This repository contains code and data related to the hERG blocker classification model eos30gr provided by Ersilia. The model predicts the probability that a molecule is a hERG blocker, with training based on 7889 compounds with experimental data (% of hERG inhibition).

## Model Information

- Model ID: eos30gr
- Slug: deepherg
- Task: Classification
- Input: Compound (SMILES)
- Output: Probability of hERG Blockade (Float)

## Steps to Reproduce

### 1. Install Ersilia Model Hub

Use this [link](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/installation) to install Ersilia Model Hub on your system

### 2. Download Model and Run

Use the following commands to download and run the model on your system. 

```
ersilia -v fetch eos30gr
ersilia serve eos30gr
ersilia -v api run -i data/input_data.csv -o data/output_data.csv
```
Note that the `input_data.csv` file is present in the data directory of this repository. If you wish to run the model on other inputs, follow [this guide](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/inputs)

### 3. Explore the Results

Open the Jupyter notebook notebooks/model_bias (eos30gr).ipynb for detailed analysis and visualizations.

## About the Dataset

The model was run on the dataset downloaded from ChEMBL in TSV format which was preprocessed to meet the model's requirements. The downloaded dataset containing 8715 entries can be viewed from `data/raw_data.tsv`.

## Results and Visualizations

The notebook provides insights into the model's predictions for 1000 molecules, including visualizations highlighting key findings.

## References

- [Ersilia GitHub Repository](https://github.com/ersilia-os/ersilia)
- [Ersilia GitBook](https://ersilia.gitbook.io/ersilia-book)
- [Model Publication](https://acrobat.adobe.com/id/urn:aaid:sc:ap:3cca2c36-6b4f-478a-996c-7f77423e819e)
- [Model GitHub Repository](https://github.com/ersilia-os/eos30gr)
- [Model Source Code](https://github.com/ChengF-Lab/deephERG)


