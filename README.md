# Analyzing the Influence of Various Factors on Global Economies

## Data Analytics (UE18CS312) Project

This repository was created with the intent of analyzing and delving deep into the numerous and diverse factors that affect economies of all countries globally, from quite obvious factors like Trade and the Finance Sector, to other parameters like Poverty, Gender and Urban & Social Development. Analysis of these variables on a macroeconomic scale is done in order to gain insight as to how developed and developing nations fare, and to see if minor improvements in any sector would lead to monumental change and growth overall. The dataset used for the project is the World Bank's World Development Indicators dataset, and can be found here: https://data.worldbank.org/indicator/

Implemented in Python.

### Execution
Run all cells in ```ridge.ipynb``` (Please note that the paths may have to be tweaked if run on Linux)

### Components
- ```Indicators.csv```: This csv file is used as reference to access the various CSVs for the indicators and has the following attributes:
  - Indicator_Code: The WDI code for the indicator
  - Indicator_Name: The name as given by the World Bank
  - included: 1 if the indicator is considered for the Ridge model, 0 if not
  - feature_name: Shortened form of Indicator_Name
- ```create_datasets.py```: This module is used to create the datasets for each year, for both developed and developing countries, clean the said data and return train test splits of the size mentioned by the user
- ```models.ipynb```: This notebook contains all the different models tried (MLR, PCA, Lasso Regression, Linear SVR and Ridge) and their performance metrics
- ```ridge.ipynb```: This notebook contains the Ridge regression model, validated using 10-Fold cross validation, along with the computed coefficients, and RMSE and accuracy scores for each year 

### Authors
- Adithi Satish
- Raksha Ramesh
- Shriya Shankar
