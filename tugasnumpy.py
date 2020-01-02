#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
data = [1,2,3]
data 


# In[3]:


np.arange(10,51)


# In[4]:


np.arange(10,51,2)


# In[29]:


np.arange(0,9).reshape(3,3)


# In[30]:


arr = np.arange(25)
arr


# In[32]:


np.random.rand(25)


# In[36]:


np.arange(1,26).reshape(5,5)


# In[42]:


arr_2d = np.array(([12, 13, 14, 15], [17, 18, 19,20],[22, 23, 24, 25]))
arr_2d


# In[48]:


arr_2d[1][3]


# In[56]:


arr.min()


# In[57]:


arr.max()


# In[55]:


arr = arr_2d[arr_2d>10]
arr[arr<=20]


# In[ ]:




