#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import scipy.stats as stats
import pylab


# In[2]:


BR = pd.read_csv("C:/Users/Dibish Babu/Downloads/BuyerRatio (1).csv")


# In[3]:


BR


# In[4]:


br = BR.drop(['Observed Values'], axis=1)


# In[8]:


#Inputs are 4 discrete variables(east,west,north,south).
#Output is also discrete. 
#We are trying to find out if proportions of male and female are similar or not across the regions
#Hence, we'll proceed with chi-square test


# In[6]:


#Create hypothesis
#Ho= Proportions of Male and Female are same
#Ha= Proportions of Male and Female are not same


# In[7]:


from scipy.stats import chi2_contingency


# In[9]:


br


# In[10]:


chi2_stat, p_val, dof, ex =stats.chi2_contingency(br) 

print("===Chi2 Stat===")
print(chi2_stat)
print("\n")
print("===Degrees of Freedom===")
print(dof)
print("\n")
print("===P-Value===")
print(p_val)
print("\n")
print("===Contingency Table===")
print(ex)


# In[11]:


#Since p-value (0.66)> alpha (0.05), hence we can't reject the null hypothesis
#Conclusion: proportion of male and female across regions is same.


# In[ ]:




