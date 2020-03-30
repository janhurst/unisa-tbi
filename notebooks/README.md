# Jupyter Notebooks
Can include Data Cleaning, EDA, ML training etc

The following notebooks are chained together, that is using %run to call one of the notebooks will result in the preceeding notebooks in descending order of their two digit prefix to also be %run.

## 00-load-raw-data.ipynb
Provides a consistent loading mechanism from the original PECARN TBI data file.

An environment variable named TBI_DIR can be used to provide the location of the original PECARN TBI CSV file.

## 01-data-cleaning.ipynb
Contains any data cleaning steps that have been determined through assessment of the dataset and incorporating Subject Matter Expert knowledge.

Also includes renaming variables/columns to more human readable forms.

## 02-data-imputation.ipynb
Any remaining NaN values are imputed using a "most frequent" strategy.
