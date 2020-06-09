#!/usr/bin/env python
# coding: utf-8

# # How do i select multiple rows and columns?

# In[1]:


import pandas as pd


# In[2]:


# ufo = pd.read_csv('http://bit.ly/uforeports')
ufo = pd.read_csv('uforeports.csv')
ufo


# - Loc sirver para filtrar filas y seleccionar columnas por label (nombres)

# In[3]:


ufo.loc[0,:]


# In[6]:


ufo.loc[:,"City"]


# In[ ]:
