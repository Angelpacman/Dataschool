#!/usr/bin/env python
# coding: utf-8

# # How do i use string methods in pandas?

# In[1]:


'hello'.upper()


# In[2]:


import pandas as pd


# In[4]:


# orders = pd.read_table('https://bit.ly/chiporders')
orders = pd.read_table('chiporders.tsv')

orders.head()


# Vamos a aprender a usar un metodo de strings dentro de una serie de pandas, para ello
# elegimos una columna, por ejemplo orders.item y le aplicamos el metodo str.contains()
# que ha de buscar en cada fila de esta columna la cadena 'Chicken' y como resutado arroja
# una serie de booleanos.

# In[5]:


orders.item_name.str.contains('Chicken')


# Con todo esto ahora es posible poder pasarle la serie de booleanos para pasarla al
# data frame a fin de que pueda filtrar los valores de la cadena que son True y con ello
# quedarnos las filas del df que contienen la cadena 'Chicken' en la columna 'item_name'

# In[6]:


orders[orders.item_name.str.contains('Chicken')]


# El metodo str tiene muchas variantes, entre ellas la de buscar un caracter de nuestro
# interes y remplazarlo por otro, en el siguiente ejemplo podemos ver que se usa dos veces
# en la misma serie para buscar la cadena '[' ó ']' y remplazarla por espacios

# In[8]:


orders.choice_description.str.replace('[', '').str.replace(']', '')


# Esta última acción se puede optimizar y hacer el srt.repace en una sola declaración:

# In[9]:


orders.choice_description.str.replace('[\[\]]', '')


# Lo que hace es poner en una lista lo que se debe remplazar es decir \[ ó \],
# atención: no quiere decir que remplace lo que hay dentro de los corchetes

# In[ ]:
