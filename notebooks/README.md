# Jupyter Notebooks
The notebooks here are the "agreed" logic/code.

## 00-load-raw-data
This notebook provides an easy way to ingest the original TBI CSV file and do some simple data type wrangling.

It can be loaded from another notebook:

```
%run 00-load-raw-data.ipynb
```

## 01-data-labelling

This notebook assigns some string-like categories to the categorical data based on the information provided in the TBI PUD Documentation 10-08-2013 Excel workbook included with the TBI dataset.

Note - this is primarily used to make it a little easier when producing Python based visualisations