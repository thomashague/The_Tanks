
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import requests
import json


# In[17]:


apikey = "b399f5a7a24bf7be63e60ce7c22d1cb6e294e92b"
url = 'https://api.census.gov/data/2013/acs1?get=NAME,B10010_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + apikey


# In[18]:


data = requests.get(url)
data2 = data.json()


# In[20]:


df = pd.DataFrame(data2)


# In[23]:


df.columns = df.iloc[0]


# In[30]:


df2= df.drop([0])
df2 = df2.rename(columns={"B10010_001E":"Median Income" , "metropolitan statistical area/micropolitan statistical area" : "Stat. Area"})


# In[31]:


Cities = df2["NAME"]
YValue = df2["Median Income"]
x_axis = np.arange(len(Cities))
plt.bar(x_axis, YValue, color="b", align="edge")
tick_locations = [value+0.4 for value in x_axis]
plt.show()

