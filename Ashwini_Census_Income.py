import pandas as pd
import requests
import csv
import matplotlib.pyplot as plt
import gzip
import json
url = "https://api.census.gov/data/2013/acs1?get=NAME,B01003_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="

# Build partial query URL
api_key = "00b903aabe78f7f08bc9b8f5651f6ba6f4f0c987"
key_url = url + api_key
print(key_url)

#income less than $10k
url1 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_002E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="
url2 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_004E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="
url3 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_005E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="
#url4 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_002E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="
#url5 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_002E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="
#url6 = "https://api.census.gov/data/2013/acs1?get=NAME,B25121_002E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key="

key_url1 = url1 + api_key
print(key_url1)

income_10kdata = requests.get(key_url1)
income_10kdata = income_10kdata.json()
income_10kdf =pd.DataFrame(income_10kdata)
income_10kdf.head()

income_10kdf.columns = income_10kdf.iloc[0]
income_10kdf = income_10kdf.drop([0])
income_10kdf = income_10kdf.rename(columns={"B25121_002E":"Income <10k" , "metropolitan statistical area/micropolitan statistical area" : "MetroCode"})
income_10kdf.head()

key_url2 = url2 + api_key
print(key_url2)

income_20kdata = requests.get(key_url2)
income_20kdata = income_20kdata.json()
income_20kdf =pd.DataFrame(income_20kdata)
income_20kdf.head()

income_20kdf.columns = income_20kdf.iloc[0]
income_20kdf = income_20kdf.drop([0])
income_20kdf = income_20kdf.rename(columns={"B25121_002E":"Income <20k" , "metropolitan statistical area/micropolitan statistical area" : "MetroCode"})
#income_20kdf.drop('NAME',axis=0)
income_20kdf.head()

key_url3 = url3 + api_key
print(key_url3)

income_30kdata = requests.get(key_url3)
income_30kdata = income_30kdata.json()
income_30kdf =pd.DataFrame(income_30kdata)
income_30kdf.head()

income_30kdf.columns = income_30kdf.iloc[0]
income_30kdf = income_30kdf.drop([0])
income_30kdf = income_30kdf.rename(columns={"B25121_005E":"Income <30k" , "metropolitan statistical area/micropolitan statistical area" : "MetroCode"})
income_30kdf.head()

ombined_incomedf = pd.merge(income_10kdf, income_20kdf, on='MetroCode', how="inner")
combined_incomedf = pd.merge(combined_incomedf, income_30kdf, on='MetroCode', how="inner")

del combined_incomedf['NAME_x']
del combined_incomedf['NAME_y']

#col_order = ['Metrocode', 'NAME', 'Income <10k','Income <20k','Income <30k']
#combined_incomedf.reindex(columns=col_order)

combined_incomedf.head()

