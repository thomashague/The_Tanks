# Dependencies
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

api_key = '3286c138a388ef8b9e598517a438a480860463e3'

url = 'https://api.census.gov/data/2013/acs1?get=NAME,B01003_001E,B25004_001E,B25077_001E,B25035_001E,B10010_001E,B15003_022E,B15003_017E,B15003_021E,B15003_022E,B15003_023E,B15003_024E,B15003_025E,B21001_002E,B21001_003E,B02008_001E,B02009_001E,B02010_001E,B02011_001E,B02012_001E,B02013_001E,B05001_002E,B05001_006E,B17001_002E,B24050_002E,B24050_005E,B24050_006E,B24050_007E,B24050_008E,B24050_009E,B24050_012E,B24050_013E,B24050_016E,B24050_020E,B24050_023E,B24050_027E,C23022_001E,B05002_013E,C05001_002E&for=congressional%20district:*&key='

key_url = url + api_key

columns = {'NAME': 'Name of District',
            'B01003_001E' : 'Total Population',
            'B25004_001E' : 'Vacant Housing Units',
            'B25077_001E' : 'Median Home Value',
            'B25035_001E' : 'Median Year Sructures Built',
            'B10010_001E' : 'Median Income',
            'B15003_022E' : 'Total w/ Bachelors',
            'B08013_001E' : 'Movers to different state',
            'B08131_001E' : 'Aggregrate Travel Time to Work',
            'metropolitan statistical area/micropolitan statistical area' : 'Area ID',
            "B15003_021E":"Associates Degree", 
            "B15003_017E":"High School Diploma", 
            "B15003_022E":"Bachelor's", 
            "B15003_023E":"Masters" , 
            "B15003_024E":"Professional" , 
            "B15003_025E":"Doctorate",
            "B21001_002E": "Veteran",
            "B21001_003E": "Non-Veteran",
            "B02008_001E":"White", 
            "B02009_001E":"African American",
            "B02010_001E":"Native American/Alaskan",
            "B02011_001E":"Asian",
           "B02012_001E": "Native Hawaiian/Pacific Islander",
            "B02013_001E":"OtherRace",
            "B05001_002E" : "U.S. citizen",
            'B05001_006E' : 'Non U.S. citizen',
            "B17001_002E" : "Income in the past 12 months below poverty level",
            "B24050_002E" : "Agriculture, forestry, fishing and hunting, and mining",
            "B24050_005E" : "Construction",
            "B24050_006E" : "Manufacturing",
            "B24050_007E" : "Wholesale Trade",
            "B24050_008E" : "Retail Trade",
            "B24050_009E" : "Transportation and warehousing, and utilities",
            "B24050_012E" : "INFORMATION",
            "B24050_013E" : "Finance and insurance, and real estate and rental and leasing",
            "B24050_016E" : "Professional, scientific, and management, and administrative and waste management services",  
            "B24050_020E" : "Educational services, and health care and social assistance",
            "B24050_023E" : "Arts, entertainment, and recreation, and accommodation and food services",
            "B24050_027E" : "Public Administration",
           "C23022_001E" : "Total Unemployed",
           "B05002_013E" : "Foreign Born",
           "C05001_002E" : "U.S. citizen, born in the United States"
           
           
          }
census_response = requests.get(key_url)
census_json = census_response.json()

dataFrame =pd.DataFrame(census_json)
dataFrame.columns = dataFrame.iloc[0]
dataFrame = dataFrame.drop([0])
dataFrame = dataFrame.rename(columns=columns)

citizenship_df = dataFrame[(dataFrame['Name of District'] == "Congressional District 45 (113th Congress), California")]
citizenship_df.head()

dataFrame.columns

citizenship_df1 = citizenship_df[['U.S. citizen', 'Non U.S. citizen','U.S. citizen, born in the United States','Foreign Born']]
citizenship_df1

## Citizenship Data

labels = ["U.S. citizen", "Non U.S. citizen"]

# The values of each section of the pie chart
sizes = [529445, 76680]

# The colors of each section of the pie chart
#colors = ["yellowgreen", "red", "lightcoral", "lightskyblue", "black", "brown",]
colors = ["#ffcc99", "#66b3ff"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
# Save Figure
plt.savefig("CitizenData.png")
plt.show()

## Immigration Data
labels1 = ["Foreign Born", "U.S. citizen, born in the United States"]

# The values of each section of the pie chart
sizes = [195827, 529445]

# The colors of each section of the pie chart

colors = ["#c2c2f0", "#ffb3e6"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels1, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.savefig("ImmigrationData.png")
plt.show()


