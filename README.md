# Predicting Traumatic Brain Injuries (TBI) in Children
This project aims to provide a decision support tool based on a machine learning predictive model for assessing the need for a CT scan
for children who present to Emergency Departments with head trama.

The predictive model is initially built from a study dataset entitled 
*Identification of children at very low risk of clinically-important brain injuries after head trauma: a prospective cohort study*
collected by the [Pediatric Emergency Care Applied Research Network](http://pecarn.org) (PECARN).

The study examined the need for a CT scan for children presenting with head trauma to emergency departments in North America with the aim of identifying children at very low risk of a clinically important traumatic brain injury (ciTBI) for whom a CT scan can be avoided.

This repository contains separate components that are being worked on in parallel. During the active project phase between March and June 2020 each team member is working from their own separate branch.

An overview of the architecture for this projects is shown below.

[![Architecture Summary](https://user-images.githubusercontent.com/16224889/80082997-b0b5b900-8587-11ea-802e-96e19a3c61fd.png)](https://user-images.githubusercontent.com/16224889/80082997-b0b5b900-8587-11ea-802e-96e19a3c61fd.png)

# Getting Started

## Study Dataset
This project requires a [study dataset](http://pecarn.org/studyDatasets/StudyDetails?studyID=4) from PECARN. Please obtain the CSV data file from PECARN and place it in the same directory as the project files.

## Conda Environment
A conda environment YAML file creating an environment named `tbi` is provided. This environment has all of the packages that have been used in the development of this work.

To create the environment run:
```
conda env create -f environments/tbi.yml
conda activate tbi
```

When executing any Python scripts or working with notebooks, please ensure the project's `src` folder is on Python's module search path (i.e. in the system path, or the ```PYTHONPATH```)

A Visual Studio Code workspace named `unisa-tbi.code-workspace` is provided, along with several workspace configuration settings. The Microsoft Python extension is recommended.

## Loading Initial Data

The raw PECARN data can be loaded via the `data.pecarn` module:
```
from data import pecarn
df = pecarn.load(fromCsv=True)
```
The ```load()``` function will read the original PECARN CSV file and convert the dataframe columns to categorical data types

> Note: The PECARN data requires that the original study dataset CSV file is placed in the same directory as the calling python script. A .pkl version of the resulting DataFrame will be cached to improve performance and will be loaded on subsequent `pecarn.load()` calls unless the `fromCsv=True` flag is set.

A "cleaned" version of the PECARN data is also available: 
```
from data import pecarn
cleaned_df = pecarn.clean(pecarn.load())
```
The cleaned dataframe is the result of logic being applied on the basis of domain knowledge, as well as removal of columns that store data that is collected during case follow up, and is not available as an input to a predictive model when a patient presents to an emergency department.

A "preprocessed" version of the data is also available:
```
from data import pecarn
X, y = pecarn.preprocess(pecarn.clean(pecarn.load()))
```

The preprocess module applies further cleaning rules to the dataframe to prepare it for consumption in a machine learning algorithm. Specifically, NaNs are imputed or otherwise removed, and categorical data is one-hot-encoded. The data is returned in an input (X) and class (y) tuple, where `PosIntFinal` is the class label.

The preprocessing logic is also available as an sklearn transformer pipeline, which can be prepended to any `sklearn.pipeline.Pipeline`:

```
from sklearn.pipeline import Pipeline

my_pipeline = Pipeline(steps=[
    ('data.pecarn.preprocess', pecarn.preprocess.make_preprocess_pipeline),
    ('my_other_transformers'), ...),
    ...
])
```
