#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import pyplot

train = pd.read_csv("./train.csv")
y = train["method"]
x = train.drop(['method','No'],axis=1)


# In[7]:


# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier()
# knn.fit(x,y)
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(x,y)


# In[9]:


test = pd.read_csv("test.csv")
ans = tree.predict(test)
ans

