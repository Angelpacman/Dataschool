#!/usr/bin/env python
# coding: utf-8

# # How do i create dummy variables?

# In[1]:


import pandas as pd


# In[2]:


train = pd.read_csv("http://bit.ly/kaggletrain")
train.head()


# - Para poder crear una dummy variable de la columna sex podemos usar el metodo de series map como se ve acontinuacion:

# In[3]:


train["Sex_male"] = train.Sex.map({'female':0, 'male':1})
train.head()


# - Existe otro metodo para crear esta variable sin en metodo map, y en un metodo de pandas llamado pd.get_dummies()

# In[5]:


pd.get_dummies(train.Sex)


# - Pero notamos que nuestro df tiene 2 columnas siendo que solo nos interesa tomar un columna, al ser unicamente male  o female los valores se convierten en 0 y 1. Cualquier columna que elejimos es util, asi que cortamos la columna que necesitamos con el metodo iloc:

# In[11]:


pd.get_dummies(train.Sex).iloc[:,1:]


# Hacemos un prefijo para agregar al prinicipio del nombre original de la columna:

# In[12]:


pd.get_dummies(train.Sex, prefix="Sex").iloc[:,1:]


# #### Hacer variables dummies de variables categoricas que tienen mas de 2 categorias:

# In[13]:


#tomaremos como referecia la volumna Embarked
train.Embarked.value_counts()


# In[14]:


pd.get_dummies(train.Embarked, prefix = "Embarked")


# In[18]:


#seleccionamos con el metodo iloc todas las columnas de la  segunda en adelante y la asignamos a una variable:

embarked_dummies = pd.get_dummies(train.Embarked, prefix = "Embarked").iloc[:,1:]
embarked_dummies


# - Y vamos a agregar esta variable a nuestro principal dataframe con el metodo de concatenar:

# In[23]:


#recordar que vuando se  quiere trabajaren torno a las columnas se utliza axis =1 y cuendo se trata de filas axis = 0
train = pd.concat([train, embarked_dummies], axis=1)
train


#  #### Ahora un truco para variables dummies

# In[26]:


#devolvemos el dataframe a su estado original
train = pd.read_csv("http://bit.ly/kaggletrain")
train.head()


# In[27]:


# Y usamos el metodo get_dummies()
pd.get_dummies(train, columns = ["Sex", "Embarked"])


# - Y como por arte de magia ha quitado las columnas que transformamos en dummies y nos devuelve las categorias de las variables en forma de series, si queremos quitar la primer columna que resulta de cada variable dummie en lugar de hacerlo con el metodo de iloc como lo hemos estado haciendo, podemos aplicar una bandera desde el mismo metodo get_dummies():

# In[28]:


pd.get_dummies(train, columns = ["Sex", "Embarked"], drop_first = True)


# In[ ]:





# In[ ]:




