#!/usr/bin/env python
# coding: utf-8

# # How do i work with dates and times in pandas?

# In[1]:


import pandas as pd


# In[4]:


ufo = pd.read_csv("uforeports.csv")
ufo.head()


# In[7]:


#examinamos los tipos de objetos que hay dentro del dataframe
ufo.info()


# In[14]:


ufo.Time.str.slice(-10,-6).value_counts()


# In[27]:


ufo.Time.str.slice(-5,-3).value_counts()


# In[28]:


ufo.Time.str.slice(-5,-3).astype(int)


# - Ahora que tenemos la hora del avistamiento convertida en int64 podemos darle un formato de fecha de pandas:

# In[29]:


ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()


# In[31]:


ufo.dtypes


# #### Transformar objetos a fechas

# - Para hacer una especie de conteo del registro de avistamiento en funcion de las horas del dia con las horas que obtuvimos de las cadenas de caracteres extraidas de la columna Time
# 
# - Pero en lugar de ello aplicamos directamente un metodo de pandas, aplicable a las horas del dia, numero de dia, dia de la semana, mes del año, etc:

# In[32]:


ufo.Time.dt.hour


# In[51]:


ufo.Time.dt.weekday


# In[49]:


ufo.Time.dt.day_name()


# In[52]:


ufo.Time.dt.day_name().value_counts()


# In[55]:


ufo.Time.dt.dayofyear


# In[79]:


ts = pd.to_datetime("9/2/2000")
ts


# In[80]:


ufo.loc[ufo.Time >= ts, :]


# ### Timedelta object

# - Si quisieramos saber cual es el tiempo exacto entre una fecha y otra que tenemos en nuestro dataframe, basta con restarle a la fecha mas reciente la fecha mas antigua:

# In[85]:


#Fecha mas reciente en el dataframe
ufo.Time.max()


# In[86]:


#Fecha mas antigua en el dataframe
ufo.Time.min()


# In[83]:


ufo.Time.max() - ufo.Time.min()


#    - Ahora que tenemos un Timedelta podemos observar que tambien tiene atributos:

# In[94]:


#tales como el de sacar el numero de dias
(ufo.Time.max() - ufo.Time.min()).days


# In[88]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[90]:


ufo['Year']=ufo.Time.dt.year
ufo.head()


# In[95]:


# Podemos hacer lo que ya sabiamos y contar por valor las veces en que se repite un anio;
ufo.Year.value_counts()


# In[95]:


# Podemos hacer lo que ya sabiamos y contar por valor las veces en que se repite un anio;
ufo.Year.value_counts()


# - Para graficar los datos es conveniente acomodar las variables por index y para eso hacemos un conteo y un ordenamiento:

# In[92]:


ufo.Year.value_counts().sort_index()


# In[93]:


ufo.Year.value_counts().sort_index().plot()


# In[ ]:




