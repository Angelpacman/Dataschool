#!/usr/bin/env python
# coding: utf-8

# # How do i remove columns from a pandas DataFrame?

# In[16]:


import pandas as pd


# In[17]:


ufo = pd.read_csv('https://bit.ly/uforeports')


# In[18]:


ufo.head()


# In[19]:


ufo.shape


# In[20]:


ufo.drop('Colors Reported', axis =1, inplace = True)
ufo.head()


# In[22]:


ufo.drop(['City', 'State'], axis=1, inplace=True)
ufo.head()


# Remover filas en lugar de columnas, esto requiere de ubicar el numero de filas que queremos fuera:

# In[23]:


ufo.drop([0,1], axis=0, inplace = True)
ufo.head()


# In[25]:


ufo.shape


# Como te puedes dar cuenta el axis se definio como 0, para que se pueda trabajar sobre las filas, con la lista que le pasamos a ufo.drop() pudimos quitar las 2 peimeras filas

# In[ ]:




