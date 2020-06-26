#!/usr/bin/env python
# coding: utf-8

# # How do I use pandas with scikit-learn to create Kaggle submissions?

# In[1]:


import pandas as pd


# - Kaggle es una plataforma para competencias de machine learning, scikit-learn es una libreria de python que se usa en ml. Es frecuentemente usado para fines educativos

# In[2]:


train = pd.read_csv('http://bit.ly/kaggletrain')
train


# In[4]:


feature_cols = ['Pclass', 'Parch']
feature_cols


# In[6]:


X = train.loc[:,feature_cols]
X


# In[7]:


y = train.Survived
y


# In[9]:


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X,y)


# In[11]:


test = pd.read_csv('http://bit.ly/kaggletest')
test


# In[13]:


X_new = test.loc[:,feature_cols]
X_new


# In[14]:


new_pred_class = logreg.predict(X_new)
new_pred_class


# In[15]:


test.PassengerId


# In[18]:


pd.DataFrame({'PassengerId':test.PassengerId,'Survived':new_pred_class})


# In[19]:


pd.DataFrame({'PassengerId':test.PassengerId,'Survived':new_pred_class}).set_index('PassengerId')


# In[20]:


pd.DataFrame({'PassengerId':test.PassengerId,'Survived':new_pred_class}).set_index('PassengerId').to_csv('sub.csv')


# In[21]:


train.to_pickle('train.pkl')


# In[22]:


pd.read_pickle('train.pkl')


# In[ ]:




