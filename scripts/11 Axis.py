#!/usr/bin/env python
# coding: utf-8

# # How do i use the "axis" parameter in pandas?

# In[20]:


import pandas as pd


# In[21]:


# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = pd.read_csv('drinks.csv')
drinks.head()


# In[22]:


drinks.shape


# La forma en que se puede eliminar una fila o columna es con la funcion drop(),
# pero que la funcion sepa que es lo que queremos quitar del df debemos asignar valor
# a la opcion "axis", a grandes rasgos;
#
# para eliminar filas:
# axis = 0
#
# para eliminar columnas:
# axis = 1

# In[23]:


drinks.drop('continent', axis = 1).head()


# In[24]:


drinks.drop(2, axis = 0).head()


# In[25]:


drinks.mean()


# In[26]:


drinks.mean(axis = 0)


# In[39]:


drinks.mean(axis = 1)


# In[28]:


drinks.mean(axis = 0).shape


# In[29]:


drinks.mean(axis = 'index')


# In[30]:


drinks.mean(axis = 1)


# In[31]:


drinks.mean(axis = 'columns')


# In[32]:


drinks.head()


# In[ ]:





# In[ ]:
