#!/usr/bin/env python
# coding: utf-8

# # task 1 remove in list

# In[2]:


x=[1,2,3,4,5,1,1,1]


# In[6]:


while(x.count(1))>0:
       x.remove(1)


# In[7]:


print(x)


#  # task 2 ascii represntation

# In[16]:


y=input("enter character ")


# In[17]:


print(ord(y))


#  # task 3 calculator

# In[60]:


x=float(input("Enter first number : "))
y=float(input("Enter second number : "))
z=input("Enter Operation : ")


# In[61]:


if (z == ''+''):
    print(x + y) 
    
elif (z == ''-''):
    print(x - y)   
    
elif (z == ''*''):
    print(x * y) 
    
elif (z == ''/''):
    print(x / y) 
    
else :
    print("ENTER OPERATION")


# 

# In[ ]:




