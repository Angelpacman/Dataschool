#!/usr/bin/env python
# coding: utf-8

# # How do i select multiple rows and columns?

# - Basicamente loc iloc y iax son metodos para seleccionar filas y columnas

# In[1]:


import pandas as pd


# In[2]:


#ufo = pd.read_csv('http://bit.ly/uforeports')
ufo = pd.read_csv('uforeports.csv')
ufo


# ## Loc

# - Loc sirve para filtrar filas y seleccionar columnas por label (cuando se habla de labels en pandas se refiere a que se selecciona par index cuando se trata de filas y  se selecciona por nombre de columnas cuando se trata de las columnas)
# 
# - La forma de usar Loc es la siguiente: .loc[ que filas quiero , que columnas quiero ]

# In[3]:


#En el ejemplo siguiente se usa el df ufo con la fila 0 y todas las columnas, que se representan con ":"
ufo.loc[0,:]


# In[4]:


#Aqui lo que buscamos es todas las filas de la columna "City"
ufo.loc[:,"City"]


# - Se pueden seleccionar filas especificas del df si se pasan al metodo loc en una lista:

# In[5]:


#En este caso elegimos de las filas con index = 0,1,2 todas las columnas ":"
ufo.loc[[0,1,2],:]


# - La forma de seleccionar varias filas que son consecutivas  es declarando el intervalo:

# In[6]:


#Esta forma arroja un resultado que es equivalente a la sentencia anterior
ufo.loc[0:2,:]


# ####  IMPORTANTE: hay que notar que la seleccion 0:2 no excluye el index = 2

# - Pasar a una lista todos los label que deseamos tambien lo podemos hacer en  las columnas:

# In[7]:


#En este ejemplo logramos que seleccione todas las filas de las columnas "City" y "State"
ufo.loc[:,["City","State"]]


# - Tambien pasar las columnas de una forma consecutiva:

# In[8]:


#En este caso logramos obtener las filas de 0 a 2 todas las columnas que hay desde "City" hasta "State"
ufo.loc[0:2,"City":"State"]


# - Como nada de esta ha sido asignado a ninguna variable, se puede obtener el resutado anterior usando el metodo .drop() y retiraremos la columna "Time" que esta en axis=1

# In[9]:


ufo.head(3).drop('Time', axis = 1)


# - Filtrando los avistamientos en Oakland usando la serie de booleanos True que coincidan con la condicion:

# In[10]:


ufo[ufo.City == 'Oakland']


# - El mismo filtro lo podemos obterner con loc de una manera bastante similar:

# In[11]:


ufo.loc[ufo.City == 'Oakland', :]


# ## iLoc

# - iloc sirve para seleccionar filas y columnas pero usando una posición que es hecha por un numero entero:

# In[12]:


# De esta manera logramos seleccionar todas las filas de las columnas que se encuentran en la posicion 0 y 3
ufo.iloc[:, [0,3]]


# - Tambien se le puede pasar una lista a iloc asi como una serie consecutiva de labels

# In[13]:


ufo.iloc[:,0:3]


# #### Cabe mencionar que en este metodo si se excluye la columna que fijamos como limite (fila con posición = 3, es decir cuarta columna)

# In[14]:


#supongamos que queremos todas las columnas de la posición 0 a 2, entonces;
ufo.iloc[0:3, :]


# ## ix function (deprecated)

# - La funcion ix es obsoleta en pandas al menos desde version 1.0

# In[15]:


drinks = pd.read_csv('drinks.csv', index_col = 'country')
drinks


# In[16]:


drinks.ix['Albania', 0]


# In[17]:


drinks.ix(1,"beer_servings")


# In[19]:


drinks.ix['Albania':'Andorra',0:2]


# In[20]:


drinks.loc['Albania':'Andorra', 'beer_servings':'spirit_servings']


# In[21]:


drinks.iloc[1:4, 0:2]


# In[ ]:




