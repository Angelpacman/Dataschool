#!/usr/bin/env python
# coding: utf-8

# # How do i handle missing values in pandas

# In[1]:


import pandas as pd


# In[4]:


# ufo=pd.read_csv('https://bit.ly/uforeports')
ufo=pd.read_csv('uforeports.csv')

ufo.head()
ufo.tail()


#    NaN significa not available number, por alguna razón, algunos set de datos no tienen el valor en el data set de alguna fila de algun campo. intentaremos trabajar con ello.
#
#    Para eso podomos usar la funcion isnull(), la cual se encarga se arrojar series de booleanos que nos permitan hacer un filtro y tomar como verdaderos los valores que son NaN, su contraparte es la funcion notnull() que se encarga de hacer lo propio con LOS VALORES QUE NO SEAN NaN.
#
#    Por último hay que agregar que para la version de pandas 0.21 (octubre 2017) las funciones que se agregan son isna() y notna() que funcionan como las librerias de null.

# In[5]:


ufo.isnull().tail()


# In[6]:


ufo.isna().tail()


# In[8]:


ufo.notnull().tail()


# In[9]:


ufo.notna().tail()


# Se puede ver que con la funcion type que al usar isna o notna el type que regresa sique siendo un dataframe de pandas, por lo que podemos usar la función sum para realizar un conteo de las variables categoricas en cada uno de los campos

# In[13]:


type(ufo.isna())


# In[14]:


ufo.isna().sum()


# Esto sucede porque al pasar una Serie de pandas a la suma, convierte los valores en booleanos y por lo tanto ceros y unos, vease el siguiente ejemplo:

# In[17]:


pd.Series([True,False,True]).sum()


# ### Filtrando los NaN en el campo City del data set:

# In[19]:


ufo.City.isna()


# Usando esa serie de booleanos para filtrar en el data set y quedarnos con las vilas que tienen el valor True de esta serie:
#

# In[20]:


ufo[ufo.City.isna()]


# In[22]:


ufo.shape


# Una vez que ya filtramos los valores que son nan, podemos pasarlo a la funcion dropna para que podamos quitar las filas que contienen NaN

# In[23]:


ufo.dropna(how='any').shape


# Con esto nos podemos dar cuenta que el tamaño del data set de ha reducido de manerea significativa, pasó de tener 18241 filas a tan solo 2486

# La funcion anterior para quitar los valores nulos es bastante agresiva debido a que quita cualquier fila que tenga un valor nulo en cualquiera de los campos
#
# Una opción aun mas especifica y menos agresiva con el recorte de los datos es cambier la opción any por all, lo que va a resultar en que los recortes de las filas solo se han de efectuar si la fila tiene NaN en todos los campos.

# In[26]:


ufo.dropna(how='all').shape


# En el caso de este data set en particular, no ha borrado ninguna fila porque los datos de la columna de las fechas están completas

# Hay una forma especial de esta misma función pero con el criterio de recorte aplicado a columnas especificas del data set, para ello dentro de la funcion dropna vamos a definir una opción que se llama subset, y esta a su vez va a tomar la forma de una lista que contenga el nombre de las columnas que queremos utilizar como criterio para el recorte de las filas

# In[28]:


ufo.dropna(subset=['City', 'Shape Reported'], how="any")


# Seguimos podiendo usar el criterio how con el subset

# In[29]:


ufo.dropna(subset=['City', 'Shape Reported'], how="all")


# ### value_counts() con valores NaN
#
# Los valores NaN no son tomados en cuenta a la hora de hacer un conteo de variables unicas en los campos. asi que si hay valores faltantes en una columna no seran tomados en cuenta para el conteo

# In[30]:


ufo['Shape Reported'].value_counts()


# Para poder contar los NaN en la función value_counts() es necesario agregar el argumento dropna=False

# In[31]:


ufo['Shape Reported'].value_counts(dropna=False)


# ### Rellenar los NaN con un valor específico

# In[34]:


ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
ufo['Shape Reported'].value_counts()


#    Como puedes ver al transformar los valores de NaN en VARIOUS se sumaron a los valores de VARIOUS que ya existian, lo que hace que se pongan a la cabeza en la función de conteo

# In[ ]:
