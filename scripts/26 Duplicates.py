#!/usr/bin/env python
# coding: utf-8

# ## How do i remove duplicate rows in pandas?

# In[1]:


import pandas as pd


# In[5]:


# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')
users.head()


# In[7]:


users.shape


# - Supongamos que queremos obtener los duplicados de los zip_code:

# In[9]:


users.zip_code.duplicated()


# In[10]:


#saber cuantos de los codigos estan duplicados
users.zip_code.duplicated().sum()


# In[12]:


users.duplicated().sum()


# - Sabemos que cada registro tiene un user_id unico pero como usamo este id como index podemos obeter filas duplicadas con los mismos datos.
# 
# 
# - Podemos usar el metodo duplicated para obtener directamente los duplicados y por defecto conserva la primer fila duplicada y los demas los descarta.
# 
# 
# - Si usamos la opcion keep dentro de duplicated podemos determinar que dato es el que queremos conservar; el primero que se repite o el segundo que se repite. o hacer keep = False, lo que significa que va a agrupar a todos los datos que se repitan.

# In[13]:


users.loc[users.duplicated(),:]


# In[18]:


users.loc[users.duplicated(keep='first'),:]


# - Asumiendo que ya sabemos que queremos conservar los primeros duplicados y eliminar el resto, podemos usar el metodo drop:

# In[19]:


users.drop_duplicates(keep='first').shape


# - Ahora podemos notar que despues de que han sido removidas las filas duplicadas nos quedan 936 filas de las 943 iniciales

# #### Quitar duplicados de filas pero solo en funcion de alguna(s) columna(s):

# In[20]:


#Supongamos que queremos obtener los duplicados que existen de edad y zip_code
users.duplicated(subset=['age', 'zip_code']).sum()


# In[24]:


#Notamos que hay 16 filas que tienen una edad y codigo postal identico, para quitarlas usamos drop:
users.drop_duplicates(subset=['age', 'zip_code']).shape


# In[ ]:




