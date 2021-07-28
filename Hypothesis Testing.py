#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[5]:


# Load the dataset
data=pd.read_csv('C:/Users/Dibish Babu/Downloads/Cutlets.csv')
data.head()


# In[8]:


#Assume Null hyposthesis as Ho: μ1 = μ2 (There is no difference in diameters of cutlets between two units)
#Thus Alternate hypothesis as Ha: μ1 ≠ μ2
#(There is significant difference in diameters of cutlets between two units) 2 Sample 2 Tail test applicable


# In[9]:


unitA=pd.Series(data.iloc[:,0])
unitA


# In[10]:


unitB=pd.Series(data.iloc[:,1])
unitB


# In[11]:


# 2-sample 2-tail ttest:   stats.ttest_ind(array1,array2)     # ind -> independent samples
p_value=stats.ttest_ind(unitA,unitB)
p_value


# In[12]:


p_value[1]     # 2-tail probability


# In[13]:


# compare p_value with α = 0.05 (At 5% significance level)


# In[14]:


#Inference: As (p_value=0.4722) > (α = 0.05); Accept Null Hypothesis i.e. μ1 = μ2
#( Thus, there is no difference in diameters of cutlets between two units


# In[ ]:




