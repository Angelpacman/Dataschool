#!/usr/bin/env python
# coding: utf-8

# # How do I make my pandas data frame smaller and faster?

# In[1]:


import pandas as pd


# In[2]:


drinks = pd.read_csv('drinks.csv')
drinks


# - Podemos ver el uso de memoria por columna con la funcion .info() ademas de que nos dice que tipo de datos se maneja en cada columna

# In[3]:


drinks.info()


# - la memoria usada es solo un estimado que arroja debido a que los datos que son objetos pueden almacenar mas informacion de la que parece (esto por trartarse de strings convinados con numeros)
# - podemos obligar a pandas para que nos de el estimado de la memoria estimada en la misma funcion .info() pero agregando un parametro;

# In[4]:


drinks.info(memory_usage='deep')


# Como podemos notar ahora nos dice el verdadero tamaño de la memoria usada, que es de aprox 30.5 KB

# In[5]:


drinks.memory_usage()


# - Para poder ver la memoria usada en KB reales podemos usar el mismo parametro en esta funcion;

# In[6]:


drinks.memory_usage(deep=True)


# - Y para poder ver la suma de toda esta memoria podemos usar la funcion sum()

# In[7]:


drinks.memory_usage(deep=True).sum()


#  #### Reducir los dtype que son object
#  
#  - Los datos que son de tipo object ocupan demasiada memoria 
#  - lo que se propone a continuacion es tomar los tipo object y almacenarlo como integers
#  - La primera duda que puede surgir es; ¿como un objeto que tiene mas forma de string puede hacerse integer?
#  - Bueno, usando un metodo de pandas lo que haremos es almacenar las variables categorias en numeros seriados y finitos, empezando en este ejemplo por los continentes, ya que es una columna que tiene muy pocos uniquevalues

# In[9]:


sorted(drinks.continent.unique())


# In[10]:


drinks.continent.head()


# In[12]:


drinks['continent'] = drinks.continent.astype('category')


# In[15]:


drinks.dtypes


# - Podemos notar que ahora el tipo de objeto de continent es category

# In[16]:


drinks.info()


# - Y nos dice que en esta columna hay 6 catogorias:

# In[17]:


drinks.continent.head()


# In[19]:


#Con esto podemos ver los codigos que fueron asignados a las catogorias para poder optimizar la memoria
drinks.continent.cat.codes.head()


# In[20]:


#Vamos a ver la memoria usada con estas modificaciones:
drinks.memory_usage(deep=True)


# #### Tipo categoria es optimizado solo si las catogorias son pocas
# 
# - Convertir a los continentes en tipo catogory funciono porque solo eran seis categorias
# - Si hemos de intentar lo mismo en la columba de country notaremos que los uniquevalues son muchos mas de los que encontramos en continent:

# In[23]:


sorted(drinks.country.unique())


# In[33]:


len(drinks.country.unique())


# - Por lo que si hacemos el proceso anterior en la columna de country, usaremos mas memoria de lo que haciamos al principio

# In[34]:


drinks['country'] = drinks.country.astype('category')


# In[35]:


drinks.memory_usage(deep=True)


# Lo que ha pasado es que astype tuvo que crear 193 codigos diferentes para la columna country (1 codigo para cada pais)

# In[36]:


drinks.country.cat.categories


# #### Es conveniente usar astype = categories solo cuando los valores unicos de la serie son muy pocos

# ##### Bonus:

# In[41]:


df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['superb', 'very good', 'good', 'excelent']})
df


# In[42]:


df.sort_values('quality')


# - Supongamos que para nosotros la quality tiene un orden logico, es decir que algunas quality's son mas relevantes que otras
# - Y lo que ahora pretendemos es que nuestro df sea ordenado por medio de quality

# In[47]:


#Esta era la vieja forma de armar la jerarquia de las categorias dentro de la asignacion
#Actualmente no sirve, btw
df['quality'] = df.quality.astype('category', categories = ['good', 'very good', 'superb', 'excelent'], ordered = True)
df.quality


# - La nueva forma de armar la jerarquizacion de las categorias es declararla por separado:

# In[58]:


from pandas.api.types import CategoricalDtype
quality_car = CategoricalDtype(['good', 'very good', 'superb', 'excelent'], ordered = True)


# In[59]:


df['quality'] = df.quality.astype(quality_car)
df


# In[57]:


df.quality


# - Ahora podemos ver que las categorias tienen gearquia y si hacemos sort al df con quality como argumento tomara en cuenta esta jerarquizacion y no el orden alfabetico que tenia antes

# In[60]:


df.sort_values('quality')


# - Esto es util porque nos permite hacer ahora un filtro en base a caracteristicas especificas que hemos definido:

# In[61]:


df.loc[df.quality > 'good',:]


# In[ ]:




