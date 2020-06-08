#!/usr/bin/env python
# coding: utf-8

# # How do i filter rows of a pandas DataFrame by column value?

# In[2]:


import pandas as pd


# In[3]:


movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[4]:


movies.shape


# Vamos a suponer que queremos solo las filas que tienen una duracion alta, entonces para ello vamos a crear una lista de python que contengan lo que nosotros queremos, despues lo pasamos como argumento a las filas y se quedaran las filas que cumlan con nuestra condicion:

# In[5]:


booleans = []
for length in movies.duration:  #comprueba su pasa lo mismo con movies['duration']
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)
            


# In[6]:


booleans[0:5]


# In[7]:


len(booleans)


# In[9]:


is_long = pd.Series(booleans)
is_long.head()


# In[10]:


movies[is_long]


# In[11]:


movies[is_long]


# In[12]:


is_long = movies.duration >= 200
is_long.head()


# In[13]:


movies[is_long]


# In[14]:


movies[movies.duration >= 200]


# In[16]:


movies[movies.genre == "Drama"]


# In[18]:


movies[movies.duration >= 200]['genre']


# In[19]:


movies.loc[movies.duration >= 200,'genre']


# In[ ]:




