#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series, DataFrame


# In[15]:


movies = pd.read_table('D:\\taskes\\movies.dat.txt', sep = '::', names = ['MovieID', 'Title', 'Tag'], engine = 'python')

movies


# In[16]:


users = pd.read_table('D:\\taskes\\users.dat.txt', sep = '::', names = ['UserID', 'Gender', 'Age', 'Occepation', 'ZipCode'], engine = 'python')

users


# In[17]:


ratings = pd.read_table('D:\\taskes\\ratings.dat.txt', sep = '::', names = ['UserID', 'MovieID', 'Rating', 'Timestap'], engine = 'python')

ratings


# In[18]:


data = pd.merge(ratings, users)

data


# In[19]:


data = pd.merge(data, movies)

data


# In[20]:


mean_rating = data.pivot_table('Rating', index = 'Title', columns = 'Gender', aggfunc = 'mean')

mean_rating


# In[21]:


mean_rating_Female = mean_rating.sort_values(by = 'F', ascending = False)

mean_rating_Female


# In[22]:


mean_rating_age = data.pivot_table('Rating', index = 'Title', columns = 'Age', aggfunc = 'mean')

mean_rating_age


# In[23]:


mean_rating_old = mean_rating_age.sort_values(by = 56, ascending = False)

mean_rating_old


# In[24]:


a = data.groupby('Title').size()

a[a >= 250]


# In[25]:


mean_rating['diff'] = mean_rating['F'] - mean_rating['M']

mean_rating.sort_values(by = 'diff', ascending = False).head(15)


# In[27]:


mean_rating['diff'] = mean_rating['M'] - mean_rating['F']

mean_rating.sort_values(by = 'diff', ascending = False).head(15)


# In[ ]:




