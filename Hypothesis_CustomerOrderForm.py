#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency


# In[2]:


df=pd.read_csv("C:/Users/Dibish Babu/Downloads/CostomerOrderForm.csv")


# In[3]:


df


# In[4]:


df.Phillippines.value_counts()


# In[5]:


df.Indonesia.value_counts()


# In[6]:


df.Malta.value_counts()


# In[7]:


df.India.value_counts()


# In[8]:


custm=np.array([[271,267,269,280],[29,33,31,20]])


# In[9]:


custm


# In[10]:


chi2_contingency(custm)


# In[11]:


# p value= 0.2771 > 0.05, so Null Hypothesis


# In[ ]:




