# The purpose of this script is to select the last day of data from Our Word in Data's 
# vaccination dataset to cut down on data loading times

import pandas as pd
import json
import time

timestr = time.strftime("%Y%m%d")

# Get data
data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')

# Get last day of data for each country
def getData(dataset):
    countries = []
    for country in dataset['location'].unique():
        dataInner = dataset[dataset.location == country]
        last_vac = dataInner.iloc[-1, :]
        countries.append(last_vac)
    return countries

parsedData = getData(data)

# Convert to dataframe 
exportData = pd.DataFrame(parsedData)

# Save as a json file
with open(f'data/last_vac_{timestr}.json', 'w') as f:
    json.dump(exportData.to_json(orient='records'), f)


