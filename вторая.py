#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import pylab


# In[4]:


cols = [ 'name', 'gender', 'birth' ]
years = range(1880, 2011)
pieces = []


for a in years:
    df  = pd.read_table('D:\\HLAM\\babynames\\yob%d.txt'%a, sep = ',', engine = 'python', names = cols)
    df['year'] = a
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True)
    
    
baby_count = data.pivot_table('birth', index = 'gender', aggfunc = 'sum')
baby_count


# In[5]:


data


# In[10]:


gender1 = data.pivot_table('birth', index = 'year', columns = 'gender', aggfunc = 'sum')
gender1


i = gender1['M']
j = gender1['F']
l = years


plt.plot(l, i, label = 'Male', color = 'blue', lw = 1.5)
plt.plot(l, j, label = 'Female', color = 'red', lw = 1.5)
plt.legend()
plt.show()


# In[11]:


data['proportion'] = data['birth']/sum(data['birth'])
data


# In[18]:


name1 = data.pivot_table('birth', index = 'year', columns = 'name', aggfunc = 'sum')
pylab.subplot(2, 2, 1)
pylab.plot(l, name1['Johnny'], color = 'blue')
pylab.title('Johnny')


pylab.subplot(2, 2, 2)
pylab.plot(l, name1['Natalie'], color = 'black')
pylab.title('Natalie')


pylab.subplot(2, 2, 3)
pylab.plot(l, name1['Bob'], color = 'purple')
pylab.title('Bob')


pylab.subplot(2, 2, 4)
pylab.plot(l, name1['Tatyana'], color = 'orange')
pylab.title('Tatyana')


# In[17]:


name1 = data.pivot_table('proportion', index = 'year', columns = 'name', aggfunc = 'sum')
pylab.subplot(2, 2, 1)
pylab.plot(l, name1['Johnny'], color = 'blue')
pylab.title('Johnny')


pylab.subplot(2, 2, 2)
pylab.plot(l, name1['Natalie'], color = 'black')
pylab.title('Natalie')


pylab.subplot(2, 2, 3)
pylab.plot(l, name1['Bob'], color = 'purple')
pylab.title('Bob')


pylab.subplot(2, 2, 4)
pylab.plot(l, name1['Tatyana'], color = 'orange')
pylab.title('Tatyana')


# In[20]:


i = []
for a in range(1880, 2011):
    j = data[data['year'] == a]
    j.sort_values('birth', ascending = False)
    i.append(j.head(1))
l = pd.concat(i, ignore_index = True)
del l['proportion']
del l['gender']
l


# In[ ]:




