#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[7]:


twoDArray = np.array([[11,15,10,6,],[10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(twoDArray)


# In[10]:


newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[11]:


print(len(twoDArray))


# In[12]:


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[14]:


print(len(newTwoDArray))


# In[15]:


print(len(newTwoDArray[0]))


# In[17]:


def accesElements(array,rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('incorrect index')
    else:
        print(array[rowIndex][colIndex])


# In[20]:


accesElements(newTwoDArray,2,1)


# In[23]:


def traverseDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# In[26]:


traverseDArray(twoDArray)


# In[24]:


def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array [i][j] == value:
                return 'The value is located index' + str(i)+" "+str(j)
    return 'The element no found'


# In[25]:


print(searchTDArray(twoDArray,8))


# In[33]:


#0=untuk baris, 1=untuk kolom
newTDArray = np.delete(twoDArray, 2, axis=1)
print(newTDArray)


# In[28]:


print(twoDArray)


# In[ ]:




