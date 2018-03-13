
# coding: utf-8

# In[200]:


# Dependencies
import json
import requests
import numpy as np
import pandas as pd


# In[201]:


api_key = 'a770489433124a44654119b16edfb8291b8efa25'


#         End Points
End Points - URL

    Base URL / Host Name                          'https://api.census.gov/data/
    + timeseries                                   2013/
    + dataset anme acronim                         acs1
    + start queary                                 ?
    + add evriables starting with get clause       get=NAME,B25003_001E,B12001_001E,C23022_001E
    + predicate clause                             &for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:
    + insert key                                   &key='

#B12001_001E = Sex by Marital status for age 15+ ** COLUNM TO BE  "M-Status-M" & "M-Status-F" &
#B25003_001E = Tenure (Owner/Renter) ** COLUMNS TO BE "owner" "Renter"
#C23022_001E = sex by full time full time employment status ** "FT emp - M" & "FT emp - F" 
# In[202]:


url_tenure = 'https://api.census.gov/data/2013/acs1?get=NAME,B25003_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key='
url_Mstatus = 'https://api.census.gov/data/2013/acs1?get=NAME,B12001_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key='
url_Employed = 'https://api.census.gov/data/2013/acs1?get=NAME,C23022_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key='


# In[203]:


#base_url = 'https://api.census.gov/data/'
#year = '2013/'
#datasetAcronym = 'acs1/'
#query = '?get='

#full_url = base_url + year + datasetAcronym
#B12001_001E = Sex by Marital status for age 15+ (total)
#B25003_001E = Tenure (Owner/Renter)
#C23022_001E = sex by full time full time employment status

#https://api.census.gov/data/2013/acs1?get=NAME,B25003_001E,B12001_001E,C23022_001E&for=state:*&key=your key here


# In[204]:


#query for tenure response
tenure_response = requests.get(url_tenure)
tenure_json = tenure_response.json()

#query for marital status response (married)
married_response = requests.get(url_Mstatus)
married_json = married_response.json()

#query for Full Time Employment response (FTE)
FTE_response = requests.get(url_Employed)
FTE_json = FTE_response.json()


#         Look at json files

# In[205]:


#view json - tenure
tenure_json[0:3]


# In[206]:


#view json for marital status
married_json[0:3]


# In[207]:


#veiw json for full time employment status
FTE_json[0:3]


#         Convert json files to data frames

# In[208]:


# Convert tenure to to Data Frame
tenure_df =pd.DataFrame(tenure_json)
tenure_df.columns = tenure_df.iloc[0]

# Convert Married to to Data Frame
married_df =pd.DataFrame(married_json)
married_df.columns = married_df.iloc[0]

# Convert FTE to to Data Frame
FTE_df =pd.DataFrame(FTE_json)
FTE_df.columns = FTE_df.iloc[0]


#         View Data Frames

# In[209]:


tenure_df.head(3)


# In[210]:


married_df.head(3)


# In[211]:


FTE_df.head(3)


#         Correct column headings

# In[212]:


#tenur
tenure_df2 = tenure_df.drop([0])
tenure_df = tenure_df2.rename(columns={"B25003_001E":"Home Owners" , "metropolitan statistical area/micropolitan statistical area" : "MSA"})
tenure_df.head()


# In[213]:


#Married
married_df2 = married_df.drop([0])
married_df = married_df2.rename(columns={"B12001_001E":"Married" , "metropolitan statistical area/micropolitan statistical area" : "MSA"})
married_df.head()


# In[214]:


#Full Time WEmployment (FTE)
FTE_df2 = FTE_df.drop([0])
FTE_df = FTE_df2.rename(columns={"C23022_001E":"FTE" , "metropolitan statistical area/micropolitan statistical area" : "MSA"})
FTE_df.head()


#         
#         
#         Combine columns

# In[215]:


tenure_df = tenure_df.drop('MSA', axis =1)
married_df = married_df.drop('MSA', axis =1)
FTE_df = FTE_df.drop('MSA', axis =1)


# In[216]:


FTE_df.head()


# In[217]:


tenure_married_FTE_df = pd.merge(tenure_df, FTE_df, on='NAME', how="inner")
tenure_married_FTE_df2 = pd.merge(tenure_married_FTE_df, married_df, on='NAME', how="inner")
tenure_married_FTE_df = tenure_married_FTE_df2
tenure_married_FTE_df.head()

