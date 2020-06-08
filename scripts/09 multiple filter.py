#!/usr/bin/env python
# coding: utf-8

# # How do i apply multiple filter criteria to a pandas DataFrame

# In[1]:


import pandas as pd


# In[3]:


movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()


# In[4]:


movies[movies.duration >= 200]


# Como especificar mas de un filtro usando booleanos?

# In[5]:


True or False


# In[6]:


True or True


# In[7]:


False or False


# In[8]:


True and False


# In[9]:


True and True


# In[11]:


#Usar el operador & unir 2 condiciones
movies[(movies.duration >= 200) & (movies.genre == 'Drama')]


# In[12]:


movies[(movies.duration >= 200) | (movies.genre == 'Drama')]


# In[14]:


(movies.duration >= 200) & (movies.genre == 'Drama')


# In[15]:


movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')]


# In[17]:


movies[movies.genre.isin(['Crime', 'Drama', 'Action'])]


# In[ ]:




