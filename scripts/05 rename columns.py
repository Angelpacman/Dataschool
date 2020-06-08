#!/usr/bin/env python
# coding: utf-8

# # How do i rename columns un a pandas DataFrame?
# 

# In[2]:


import pandas as pd


# In[3]:


ufo = pd.read_csv('https://bit.ly/uforeports')


# In[4]:


ufo.head()


# In[5]:


ufo.columns


# In[6]:


ufo.rename(columns = {'Colors Reported':'Colors Reported', 'Shape Reported': 'Shape_Reported'}, inplace = True)


# In[7]:


ufo.columns


# In[8]:


#crealr una lista de python y usarla para remplazar los encabezados de un dataframe 
#(siempre y cuando sus tamaños coincidad)
ufo_cols=['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.head()


# In[9]:


# se puede renombrar las columnas desde el momento en que se arma el dataset, 
# se usa la opcion names dentro de read.csv y se usa header = 0 lo que significa que 
# tiene el indice=0 ( que esla primera fila) para colocarse
ufo = pd.read_csv('https://bit.ly/uforeports', names = ufo_cols, header = 0)
ufo.head()


# In[10]:


# tambien podemos cambiar le nombre de todas las columnas de un solo golpe haciendo una funcion
# que remplace los espacios de las cadenas de texto por un guion bajo, claro eso en el caso de que 
# queramos tener todos los encabezados con nombres que no contengan espacios
# ya sabras la utilidad de esta tarea ;) 
ufo = pd.read_csv('https://bit.ly/uforeports')
ufo.columns = ufo.columns.str.replace(' ' , '_')
ufo.head()


# In[ ]:




