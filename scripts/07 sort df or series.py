#!/usr/bin/env python
# coding: utf-8

# # How do i sort a pandas DataFrame or Series?

# In[1]:


import pandas as pd


# In[3]:


# movies = pd.read_csv('http://bit.ly/imdbratings')
movies = pd.read_csv('imdbratings.csv')

movies.head()


# Lo primero que aprenderemos es a ordenar una serie, y organizaremos los valores

# In[4]:


movies.title.sort_values()


# Lo cual tambien equivale a hacerlo con la notacion de bracketts

# In[7]:


movies['title'].sort_values()


# Podemos ordenar la serie pero en forma descendente con la opcion ascending = False

# In[8]:


movies['title'].sort_values(ascending=False)


# In[10]:


movies['title']


# Esto que va acontinuacion puede ordenar el dataframe completo en funcion de alguna de sus columnas, esto no afecta la posicion de las columnas solo las filas seran reacomodadas simultaneamente en funcion del orden que le pasemos, en este caso ordenar por title:

# In[13]:


movies.sort_values('title')


# In[19]:


movies.sort_values(['content_rating', 'duration'])


# In[ ]:
