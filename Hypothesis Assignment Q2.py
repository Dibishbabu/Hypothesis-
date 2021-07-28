#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[2]:


df=pd.read_csv("C:/Users/Dibish Babu/Downloads/LabTAT.csv")


# In[3]:


df.dtypes


# In[4]:


df.head()


# In[5]:


stats.f_oneway(df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],df.iloc[:,3])


# In[ ]:




