#!/usr/bin/env python
# coding: utf-8

# # What do i need to know about the pandas index? part II

# In[31]:


import pandas as pd


# In[32]:


# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = pd.read_csv('drinks.csv')

drinks


# In[33]:


drinks.continent


# In[34]:


drinks.set_index('country', inplace = True)
drinks


# - Al seleccionar una columna del data frame y hacer que nos muestre un head, nos arroja una tabla

# In[35]:


drinks.continent.head()


# - Tabla en la que aparecen los nombres de los paises actuando como index, si contamos cada vez que aparece un valor por continente con la funcion .value_counts() ahora los continentes actual como index

# In[36]:


drinks.continent.value_counts()


# - Para poder ver los indices que maneja cualquier tabla resultado de filtros, selecciones y agrupaciones podemos usar el metodo .index

# In[37]:


drinks.continent.value_counts().index


# - Asi mismo tambien podemos acceder a los valores de la tabla con el método .values (este metodo es diferente de la funcion .value_counts( ) )

# In[38]:


drinks.continent.value_counts().values


# - En este punto de la tabla que tenemos por conteo de valores por continente  podemos hacer una consuta para saber el valor de un continente poniendo su nombre en una lista (ya sabemos que el filtro y la consuta de datos puede funcionar como una comparativa de booleanos donde acabará mostrando los True):

# In[39]:


drinks.continent.value_counts()['Africa']


# - A la tabla resultante tambien podemos clasificar los valores de manera ascendente:

# In[40]:


drinks.continent.value_counts().sort_values()


# - En caso de que lo que necesitamos es esta misma tabla pero ordenado en funcion de su nombre y no de su valor, y asumiendo que el nombre y el valor del index son el mismo, podemos ordenar por index:

# In[41]:


drinks.continent.value_counts().sort_index()


# ### Construir una serie de pandas from scratch

# - Podemos armar una serie de pandas tan solo con la funcion pd.Series() poniendo una lista como argumento y un nombre dentro de las opciones:

# In[42]:


people = pd.Series([3000000, 85000], name = 'population')
people


# - Pero el index por defecto es numerado desde el cero en adelante con numeros enteros, asi que si deseamos tener un indice personalizado debemos agregarlo en las opciones de la serie:

# In[43]:


people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name = 'population')
people


# - People ahora es una serie de pandas a la cual le podemos hacer operaciones, por elemplo multiplicarla con con la columna drinks.beer_servings, el resultado es que solo Albania y Andorra obtienen valores distintos de NaN porque la serie people solo tiene 2 valores numerico que provienen en la serie:

# In[44]:


drinks.beer_servings * people


# - Podemos agregar la columna de population a nuestro df drinks con la funcion pd.concat() y como argumento una lista que tenga el nombre del df seguido del nombre de la serie que queremos agregar y ademas especificar en que direccion vamos a agregar la serie, para este caso cuando de trata de columbasa axis=1

# In[45]:


pd.concat([drinks, people], axis=1).head()


# - Una forma de agregar una columna al df es declararla como si exsistiera utilizando la notación corchetes:

# In[46]:


drinks['people'] = people
drinks


# - Hay que tener cuidado con esta asignacion, debido a que se declara que una columna va a ser parte del df que ya teniamos, esta columna se mantendra en el df hasta que sea removida

# In[ ]:
