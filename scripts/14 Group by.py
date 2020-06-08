#!/usr/bin/env python
# coding: utf-8

# # When should i use a "groupby" in pandas?

# In[9]:


import pandas as pd


# In[10]:


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[14]:


drinks.beer_servings.mean()


# Bien, ahora; ¿que pasaría si nosotros queremos hacer un analisis de los datos por continente? Lo que debemos de hacer es usar la funcion groupby tomando como argumento la columna continente

# In[12]:


drinks.groupby('continent').beer_servings.mean()


# Vamos a filtrar en este ejemplo el data frame solo por un continente:

# In[26]:


drinks[drinks.continent == "North America"].beer_servings.mean()


# In[ ]:





# In[37]:


drinks.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean'  ])


# In[39]:


drinks.groupby('continent').mean()


# A la informacion que obtuvimos de filtrado y analisis estadistico le podemos agregar un a visualizacion con matplotlib en la misma sentencia, para poder mostrar el gráfico en la notebook de jupyter se necesita poner ls sentencia de matplotlib inline al principio

# In[41]:


get_ipython().run_line_magic('matplotlib', 'inline')
drinks.groupby('continent').mean().plot(kind='bar')


# Esto de enseguida es una serie de experimentos, se intentó usar las funciones sum() para contar la suma acumulada de cada variable, asi como la funcion count() que nos ayuda a contar el numero de registros de la valiable.

# In[29]:


drinks.groupby('continent').sum()


# In[30]:


drinks.groupby('continent').count()


# In[32]:


drinks.groupby('continent').continent.count()


# In[33]:


drinks.continent.count()


# In[35]:


drinks.shape


# In[ ]:




