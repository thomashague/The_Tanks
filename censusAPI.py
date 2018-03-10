
# coding: utf-8

# In[97]:


# Dependencies
import json
import requests


# In[98]:


api_key = '3286c138a388ef8b9e598517a438a480860463e3'


# In[99]:


url = 'https://api.census.gov/data/2013/acs1?get=NAME,B01003_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key='
#url = 'https://api.census.gov/data/2016/acs1?get=*&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key='

key_url = url + api_key


# In[100]:


#base_url = 'https://api.census.gov/data/'
#year = '2016/'
#datasetAcronym = 'acs1/'
#query = '?get='

#full_url = base_url + year + datasetAcronym

#https://api.census.gov/data/2013/acs1?get=NAME,B02015_009E,B02015_009M&for=state:*&key=your key here


# In[101]:


census_response = requests.get(key_url)
census_json = census_response.json()


# In[102]:


census_json

