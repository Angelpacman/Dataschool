#!/usr/bin/env python
# coding: utf-8

# ### How do i select a pandas series from a DataFrame?

# In[1]:


import pandas as pd


# In[3]:


#pd.read_table puede leer una tabla pero se necesita csv para poder hacerlo con un 
#archivo qeu esta separado por comas

ufo = pd.read_csv("https://bit.ly/uforeports")


# In[4]:


ufo.head()


# In[5]:


type(ufo["City"])


# In[6]:


ufo.City


# In[9]:


ufo['Colors Reported']


# In[11]:


ufo.info()


# In[12]:


#arrojar la forma del data set
ufo.shape


# In[13]:


ufo.head


# In[14]:


#se pueden concaternar las columnas cuando sus valores son cadenas de caracteres
'ab' + 'cd'


# In[15]:


ufo.City + ufo.State


# In[18]:


#para agregar una columna en el df si tienen que usar los corchetes
ufo['Location'] = ufo.City + ufo.State


# In[19]:


ufo.head()

