#!/usr/bin/env python
# coding: utf-8

# # What do i need to know about the pandas index?

# In[1]:


import pandas as pd


# In[3]:


# drinks=pd.read_csv('http://bit.ly/drinksbycountry')
drinks=pd.read_csv('drinks.csv')
drinks.head()


# In[4]:


drinks


# In[5]:


drinks.index


# In[6]:


drinks.columns


# In[7]:


drinks.shape


# ### Propósito de los index
#
# Los index existen por 3 razones, identificación,selección y alineación

# In[11]:


pd.read_table('http://bit.ly/movieusers', header = None, sep= '|').head()


# In[13]:


drinks[drinks.continent == 'South America']


# La función loc nos permite identificar el contenido del campo en el indice y la columna que le especifiquemos

# In[14]:


drinks.loc[23, 'country']


# In[15]:


drinks.set_index('country', inplace = True)
drinks


# In[18]:


drinks.describe()


# In[19]:


drinks.describe().index


# In[20]:


drinks.describe().columns


# In[22]:


drinks.describe().loc['25%','beer_servings']


# In[ ]:
