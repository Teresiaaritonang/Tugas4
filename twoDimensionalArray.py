#!/usr/bin/env python
# coding: utf-8

# In[10]:


shoppingList = ['milk', 'cheese', 'butter']


# In[11]:


for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
empty = []
for i in empty:
    print('i am empty')


# In[22]:


#update/insert-list

myList = [1,2,3,4,5,6,7]
print(myList)


# In[23]:


myList.insert(4,15)
print(myList)


# In[24]:


myList.append(55)
print(myList)


# In[25]:


newList = [11,12,13,14]
print(myList)


# In[26]:


myList.extend(newList)
print(myList)


# In[27]:


myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


# In[32]:


#searching for an elements in the list
myList = [10,20,30,40,50,60,70,80,90]

def searchinList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))


# In[33]:


#list operations/ functions
total = 0
count = 0
while(true):
    inp= input('enter a number')
    if inp == 'done': break
        value = float(inp)
        numlist.append(value)
        
average = sum(numlist) / len(numlist)
print('Avarage:' average)


# In[ ]:




