# Predicting Traumatic Brain Injuries (TBI) in Children
This project aims to provide a decision support tool based on a machine learning predictive model for assessing the need for a CT scan
for children who present to Emergency Departments with head trama.

The predictive model is initially built from a study dataset entitled 
*Identification of children at very low risk of clinically-important brain injuries after head trauma: a prospective cohort study*
collected by the [Pediatric Emergency Care Applied Research Network](http://pecarn.org) (PECARN).

The study examined the need for a CT scan for children presenting with head trauma to emergency departments in North America with the aim of identifying children at very low risk of a clinically important traumatic brain injury (ciTBI) for whom a CT scan can be avoided.

This repository contains separate components a that are being worked on in parallel. During the active project phase between March and June 2020 each team member is working from their own separate branch, and these are not being actively rebased.

An overview of the architecture for this projects is shown below.

[![Architecture Summary](https://user-images.githubusercontent.com/16224889/80082997-b0b5b900-8587-11ea-802e-96e19a3c61fd.png)](https://user-images.githubusercontent.com/16224889/80082997-b0b5b900-8587-11ea-802e-96e19a3c61fd.png)

# Getting Started
Clone this project and obtain the study data set and place it in the same directory as the project clone.

[Visual Studio Code](https://code.visualstudio.com/), and the [Anaconda Python](https://www.anaconda.com/distribution/) distribution are recommended.

A Visual Studio Code workspace file is provided.

## Study Dataset
This project requires a [study dataset](http://pecarn.org/studyDatasets/StudyDetails?studyID=4) from PECARN. Please obtain the CSV data file from PECARN and place it in the same directory as the project files.

## Python Environment
A ```requirements.txt``` file is provided with the versions of selected packages used in this project. A Python virtual environment suitable to run the various scripts or modules can be created using the Python ```venv``` module:

```
python -m venv .venv
.venv\Scripts\activate
```

When executing any Python scripts or working with notebooks, please ensure the project's `src` folder is on Python's module search path (i.e. in the system path, or the ```PYTHONPATH```)

A Visual Studio Code workspace named `tbi.code-workspace` is provided, along with several workspace configuration settings. The Microsoft Python extension is recommended.

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

As well as domain logic, NaN values are also imputed, with a 0 value imputed for boolean-like data, 'most-frequent' imputed for categorical data, and 'mean' imputed for numeric data.

A "preprocessed" version of the data is also available:
```
from data import pecarn
preprocessed_df = pecarn.preprocess(pecarn.clean(pecarn.load()))
```

The preprocess module applies further cleaning rules to the dataframe to prepare it for consumption in a machine learning algorithm. Specifically, the datatypes of all variables is converted into `float64`. This can be incorporated into a sklearn pipeline. 

An example training pipeline, including sending results into [Neptune AI](https://neptune.ai) is provided in [src/train/sklearn/train_decisiontreeclassifier.py](https://github.com/janhurst/capstone/blob/master/src/train/sklearn/train_decisiontreeclassifier.py)

## Docker Image
A Docker image providing a web user interface to assess patients can be built using the provided Dockerfile:
```
docker build -t <repo>/<image>:<tag> .
```

An image for the master branch has been pushed to [Docker Hub](https://hub.docker.com/repository/docker/janhurst/unisa-tbi) with the tag ```janhurst/unisa-tbi:latest```. This image can be run locally and can be linked to a Neptune AI repository via environment variables:
```
docker run -p 8000:80 -e NEPTUNE_PROJECT="unisa-tbi/unisa-tbi" -e NEPTUNE_API_TOKEN=<your_token> -t janhurst/unisa-tbi:latest
```
The Docker image is temporarily deployed to [https://unisa-tbi.azurewebsites.net](https://unisa-tbi.azurewebsites.net).