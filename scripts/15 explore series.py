#!/usr/bin/env python
# coding: utf-8

# # How do i explore pandas series?

# In[1]:


import pandas as pd


# In[4]:


# movies = pd.read_csv('https://bit.ly/imdbratings')
movies = pd.read_csv('imdbratings.csv')
movies.head()


# In[7]:


movies.dtypes


# In[8]:


movies.genre.describe()


# In[11]:


movies.genre.value_counts()


# In[13]:


movies.genre.value_counts(normalize=True)


# In[14]:


movies.genre.unique()


# In[15]:


movies.genre.nunique()


# In[16]:


pd.crosstab(movies.genre, movies.content_rating)


# In[17]:


z = movies.genre.value_counts(normalize=True)


# In[27]:


sum(z)


# In[28]:


movies.duration.describe()


# In[29]:


movies.duration.mean()


# In[31]:


movies.duration.value_counts()


# In[32]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


movies.duration.plot(kind='hist')


# In[37]:


movies.genre.value_counts()


# In[38]:


movies.genre.value_counts().plot(kind = "bar")


# In[42]:


movies.genre.value_counts().plot(kind = "bar").invert_xaxis()


# In[62]:


pd.crosstab(movies.genre=='Action', movies.content_rating)


# In[65]:


pd.crosstab(movies['genre'][:], movies.content_rating)


# In[ ]:





# In[ ]:
