
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


vector_row = np.array([1, 2, 3])


# In[3]:


print (vector_row)


# In[4]:


vector_column = np.array([[1],
                          [2],
                          [3]])


# In[5]:


print (vector_column)


# In[6]:


import numpy as np


# In[7]:


matrix = np.array([[1, 2],
                   [1, 2],
                   [1, 2]])


# In[8]:


print (matrix)


# In[9]:


import numpy as np 
from scipy import sparse 


# In[10]:


matrix = np.array ([[0, 0],
                    [0, 1],
                    [3, 0]])


# In[11]:


print (matrix)


# In[12]:


# CSR матрица
matrix_sparse = sparse.csr_matrix(matrix)


# In[13]:


print (matrix_sparse)


# In[14]:


matrix_large = np.array ([[0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0],
                          [3, 0, 0, 0, 0, 0]])


# In[15]:


print(matrix_large)


# In[16]:


matrix_large_sparse = sparse.csr_matrix(matrix)


# In[18]:


print (matrix_large_sparse)


# In[19]:


import numpy as np
vector = np.array([1, 2, 3, 4, 5, 6])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# In[20]:


vector[2]


# In[21]:


matrix[1,1]


# In[22]:


vector[:]


# In[24]:


vector[:3]


# In[25]:


vector[3:]


# In[26]:


vector[-1]


# In[27]:


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# In[28]:


matrix[:2,:]


# In[29]:


matrix[:,1:2]


# In[30]:


import numpy as np


# In[31]:


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])


# In[32]:


matrix.shape


# In[33]:


matrix.size


# In[34]:


matrix.ndim

