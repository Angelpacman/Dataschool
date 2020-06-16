#!/usr/bin/env python
# coding: utf-8

# # When should i use "inplace" parameter in pandas?

# In[1]:


import pandas as pd


# In[10]:


ufo = pd.read_csv('uforeports.csv')
ufo


# In[3]:


ufo.shape


# In[4]:


ufo.drop("City", axis = 1).head()


# In[12]:


ufo.head()


# #### inplace
# - Cuando hacemos un drop pero el resultado no es asignado a la variable lo que sea que hayamos quitado del df no es permanente, debido a que el parametro inplace por defecto es False. Cambiar este parametro a True haria que el df tome la nueva forma de lo que hayamos quitado con la función .drop()

# In[11]:


ufo.drop("City", axis = 1, inplace = True)


# In[13]:


ufo.head()


# In[14]:


ufo.dropna(how='any')


# In[16]:


ufo.shape


# In[17]:


ufo.head()


# In[18]:


ufo.dropna(how='any', inplace=True)
ufo.head()


# - Otra forma de hacer permanente un df modificado sin usar inplace podria ser asignar la operacion al mismo df

# In[20]:


ufo.set_index('Time')
ufo.head()


# In[21]:


#De la forma anterior no modifica de manera permanente el df como vemos con este .head()
ufo.head()


# - La manera de hacerlo permanente pero sin usar inplace sería:

# In[22]:


ufo = ufo.set_index('Time')


# In[23]:


#Hacemos otro head para confirmar que los cambios ya son permanentes en el df ufo
ufo.head()


# In[ ]:




