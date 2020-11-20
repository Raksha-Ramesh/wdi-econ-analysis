import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 
from sklearn.model_selection import train_test_split

years = [str(i) for i in range(2008,2018)]
def createData():
    indicatorList = pd.read_csv('Indicator.csv')

    indicatorsToPick = indicatorList[indicatorList['included']==1]
    gdp_percap = indicatorsToPick[indicatorsToPick['feature_name']=='gdp_percap']
    indicatorsToPick = indicatorsToPick.drop(index=2) # GDP is Index 2

    def getDF(code):
        path = os.getcwd() + "\Datasets\\"
        newPath = path + code
        df = pd.read_csv(newPath + "\\" + os.listdir(newPath)[0])
        return df

    indicators = list(indicatorsToPick.Indicator_Code)
    features = []
    target = getDF("NY.GDP.PCAP.KD.ZG")

    for i in indicators:
        features.append(getDF(i))

    attributes = list(indicatorsToPick.feature_name)

    Developed = set(["Andorra","Austria","Belgium","Cyprus","Czech Republic","Denmark","Estonia","Faroe Islands","Finland","France","Germany","Greece","Guernsey","Holy See","Iceland","Ireland","Italy","Jersey","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Monaco","Netherlands","Norway","Portugal","San Marino","Slovakia","Slovenia","Spain","Sweden","Switzerland","United Kingdom","Hong Kong","Israel","Japan","Macau","Singapore","South Korea","Taiwan","Bermuda","Canada","Puerto Rico","United States","Australia","New Zealand"])

    Developing = set(features[0]['Country Name'])
    Developing -= Developed

    dev = [None]*(len(features)+1)
    dev1 = [None]*(len(features)+1)
    n = len(features)

    for i in range(n):
        dev[i] = features[i][features[i]['Country Name'].isin(Developed)]
        dev1[i] = features[i][features[i]['Country Name'].isin(Developing)]

    # i+=1
    dev[n] = target[target['Country Name'].isin(Developed)]
    dev1[n] = target[target['Country Name'].isin(Developing)]

    def createDataset(year,dfList):
        factors = [dfList[0]["Country Name"]]
        for x in dfList:
            factors.append(x[year])
        df = pd.concat(factors,axis =1, sort = False)
        # print(df.head)
        df.columns = ['country'] + attributes + ['gdp_percap']
        total_rows = max(df.count())
        
        return df

    developed = [createDataset(i,dev) for i in years]
    developing = [createDataset(i,dev1) for i in years]

    return (developed, developing)

# Example: developed,developing = createData()

#  Cleaning the Data 

# - Removing all rows with missing values for GDP
# - Median replacement for all other parameters

def cleanData(df):
    ### 1. Removing all rows that have NaNs/missing values in the target attribute
    for i in range(len(years)):
        df[i] = df[i].dropna(subset=["gdp_percap"])

    ### 2. Median replacement of missing values for the other features
    for i in range(len(years)):
            #print("\n\n\n",years[i])
            for j in df[i].iloc[:,1:]:
                df[i][j] = df[i][j].fillna(np.nanmedian(df[i][j]))

# EXAMPLE:
# cleanData(developed)
# cleanData(developing)

def checkLinearRelationship(df):
    for j in df.iloc[:,1:-1]:
        plt.title("GDP vs "+j)
        plt.scatter(df[j],df.gdp_percap)
        plt.show()

def createSplits(index, dev, size): # index indicates the year i.e. 2010-2018 is mapped to 0-9
    devyear = dev[index]
    gdpyeardev = devyear[['gdp_percap']]
    devyear = devyear.drop(columns=['country','gdp_percap'])

    if size==0:
        return(devyear,gdpyeardev)

    X_train, X_test, y_train, y_test = train_test_split(devyear,gdpyeardev,test_size=size, random_state=0)
    return (X_train, X_test, y_train, y_test)