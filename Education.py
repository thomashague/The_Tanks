
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import requests
import json


# In[59]:


apikey = "b399f5a7a24bf7be63e60ce7c22d1cb6e294e92b"
url = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_017E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey
url2 = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_021E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey
url3 = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_022E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey
url4 = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_023E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey
url5 = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_024E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey
url6 = 'https://api.census.gov/data/2013/acs1?get=NAME,B15003_025E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey


# In[14]:


educationdata = requests.get(url)
edudata = educationdata.json()
edudf =pd.DataFrame(edudata)
edudf.columns = edudf.iloc[0]


# In[15]:


edudf.head()


# In[34]:


edudf2 = edudf.drop([0])
edudf3 = edudf2.rename(columns={"B15003_017E":"High School Diploma" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
edudf3.head()


# In[39]:


associatesdegree = requests.get(url2)
addata = associatesdegree.json()
addf =pd.DataFrame(addata)
addf.columns = addf.iloc[0]


# In[40]:


addf2 = addf.drop([0])
addf3 = addf2.rename(columns={"B15003_021E":"Associates Degree" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
addf3.head()


# In[49]:


bacherlorsdegree = requests.get(url3)
bachdata = bacherlorsdegree.json()
bddf =pd.DataFrame(bachdata)
bddf.columns = bddf.iloc[0]


# In[50]:


bddf2 = bddf.drop([0])
bddf3 = bddf2.rename(columns={"B15003_022E":"Bachelor's" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
bddf3.head()


# In[52]:


mastersdegree = requests.get(url4)
mdata = mastersdegree.json()
mddf =pd.DataFrame(mdata)
mddf.columns = mddf.iloc[0]


# In[53]:


mddf2 = mddf.drop([0])
mddf3 = mddf2.rename(columns={"B15003_023E":"Masters" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
mddf3.head()


# In[55]:


profdegree = requests.get(url5)
pdata = profdegree.json()
pddf =pd.DataFrame(pdata)
pddf.columns = pddf.iloc[0]


# In[56]:


pddf2 = pddf.drop([0])
pddf3 = pddf2.rename(columns={"B15003_024E":"Professional" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
pddf3.head()


# In[60]:


doctoratedegree = requests.get(url6)
ddata = doctoratedegree.json()
dddf =pd.DataFrame(ddata)
dddf.columns = dddf.iloc[0]


# In[61]:



dddf2 = dddf.drop([0])
dddf3 = dddf2.rename(columns={"B15003_025E":"Doctorate" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})
dddf3.head()
# dddf2 = dddf.rename(columns={"B15003_025E":"Doctorate" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})


# In[62]:


dddf4 = dddf3.drop('Stat. Area', axis =1)
dddf4.head()


# In[65]:


pddf4 = pddf3.drop('Stat. Area', axis =1)
edudf4 = edudf3.drop('Stat. Area', axis =1)
addf4 = addf3.drop('Stat. Area', axis =1)
bddf4 = bddf3.drop('Stat. Area', axis =1)
mddf4 = mddf3.drop('Stat. Area', axis =1)
dddf4 = dddf3.drop('Stat. Area', axis =1)


# In[67]:


newdata = pd.merge(pddf4, edudf4, on='NAME', how="inner")
newdata2 = pd.merge(newdata, addf4, on="NAME",how = "inner")
newdata3 = pd.merge(newdata2, bddf4, on="NAME", how = "inner")
newdata4 = pd.merge(newdata3, mddf4, on="NAME", how="inner")
newdata5 = pd.merge(newdata4, dddf4, on="NAME", how="inner")
newdata5.head()

