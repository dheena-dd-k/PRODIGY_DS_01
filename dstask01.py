#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


dd=pd.read_csv("HR Records.csv")
dd


# In[21]:



plt.bar(dd["DistanceFromHome"],dd["DailyRate"])
plt.title("data")
plt.show()


# In[22]:


dd['Age'].hist()


# In[23]:


plt.scatter(dd['TotalWorkingYears'],dd['YearsInCurrentRole'])
plt.show()


# In[ ]:




