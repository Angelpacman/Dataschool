#!/usr/bin/env python
# coding: utf-8

# # How do i change the data type of a pandas series?

# In[1]:


import pandas as pd


# In[4]:


# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = pd.read_csv('drinks.csv')

drinks.head()


# In[6]:


drinks.dtypes


# Vamos a convertir "beer_servings" de entero a flotante usando un metodo string

# In[10]:


drinks['beer_servings']=drinks.beer_servings.astype(float)


# In[11]:


drinks.dtypes


# ### Asignar el tipo de objeto de las columnas antes de importar el csv al data frame

# Es un hecho que para hacer esto lo que debemos saber previeamente es el tipo de variable
# que tiene cada columna y cambiarla segun sea el caso y desde luego, asegurarnos de que
# el cambio del tipo de objeto es cambiable.
#
# Lo que podemos hacer es modificar las opciones por defecto la funcion df.read_csv()

# In[14]:


# orders = pd.read_table('http://bit.ly/chiporders')
orders = pd.read_table('chiporders.tsv')

orders.head()


# In[15]:


orders.dtypes


# In[17]:


#Como podemos observar el precio de los articulos es un tipo objeto, y esto se debe a que los precios
#estan capturados con "$", lo cual lo hace una mezcla entre objetos y numeros. Por ello es que vamos a
#remplazar "$" y vamos a convertirlo a flotante antes de realizarle cualquier operacion matematica

orders.item_price.str.replace('$','').astype(float).mean()


# El siguiente ejemplo tiene muchas aplicaciones, vamos a convertir una serie de booleanos no
# solo para filtrar el data frame sino para convertirlo en ceros y unos, esto puede usarde en
# una matriz de machine learning y ver que filas contienen o no una caracteristica de nuestro
# interes pasandole a la matriz los numeros que los definen:

# In[20]:


orders.item_price.str.contains('Chicken').astype(int)


# In[ ]:
