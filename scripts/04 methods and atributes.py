#!/usr/bin/env python
# coding: utf-8

# # Why do some pandas commands end with parentheses, and other commands don't?

# In[1]:


import pandas as pd


# In[2]:


# movies = pd.read_csv('https://bit.ly/imdbratings')
movies = pd.read_csv('imdbratings.csv')


# In[3]:


movies.head()


# In[6]:


movies.shape


# El atributo shape nos dice las dimensiones que el dataframe tiene, y el dtypes nos dice el
# tipo de objeto que tiene cada columna en el dataset

# In[7]:


movies.dtypes


# In[9]:


type(movies)


# In[12]:


#Este metodo describe de manera estadistica las columnas pero solo las que tienen valores numéricos
movies.describe()


# La razon es la diferencia entre metodos y atributos, un metodo usa parentesis mientras que
# os atributos se escriben despues del objeto y un punto
#

# In[13]:


#para desribir las columnas pero ahora solo haciendo caso a las que tienen variables tipo object
movies.describe(include=['object'])


# ### Importante; para obtener info sobre las funciones lo que se tiene que hacer es colocar
# el cursor en el parentesis y presionar SHIFT + TAB

# In[ ]:
