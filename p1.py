#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python program using Matplotlib
# for forming a linear plot

# importing the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(20,30, 100, 100)

# Plot the data
plt.plot(x, x, label ='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[ ]:




