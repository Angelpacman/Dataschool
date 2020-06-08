#!/usr/bin/env python
# coding: utf-8

# # How so i read a tabular data File into pandas

# In[1]:


import pandas as pd


# In[3]:


orders = pd.read_table('http://bit.ly/chiporders')


# In[5]:


orders.head()


# En el caso anterior los datos estan bien acomodados y tienen su encabezado bien definido, sin embargo, hay ocaciones en las que los datos no estan bien separados como en el siguiente ejemplo:

# In[7]:


pd.read_table('http://bit.ly/movieusers')


# para poder definir los se paradores de usa la opcion "sep" para poder definir que es lo que ha de actuar como un separador:

# In[8]:


pd.read_table('http://bit.ly/movieusers', sep ="|")


# Bien, ahora los datos ya estan bien separados, pero tienen el problema de que no tienen encabezado y de hecho pandas por defecto toma la primera fila (row) de un dataframe como si fuera el encabezado, en el siguiente ejemlo le damos a entender a pandas que no existe un encabezado como tal y que todas las filas son solamente observaciones de la variable.

# In[9]:


pd.read_table('http://bit.ly/movieusers', sep ="|", header = None)


# Ahora ya tenemos los datos con columnas numeradas ya que no tienen ningun encabezado por defecto, asi que hemos de asignar ahora un encabezado haciendo uso de una lista que nosotros mismos podemos hacer:
# 

# In[10]:


user_cols = ['user_id', 'age', 'gender', 'pccupation', 'zip_code']
pd.read_table('http://bit.ly/movieusers', sep ="|", header = None, names = user_cols)


# #### hay una opción mas que se llama skipfooter, se puede usar a la hora de asignar los datos, y sirve en el caso de que el archivo que contiene los datos tiene algun tipo de notas al final o al principio

# In[ ]:




