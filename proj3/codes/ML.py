# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from matplotlib import pyplot


# %% [markdown]
# Use pandas to read .csv files

# %%
train = pd.read_csv("./train.csv")

# %% [markdown]
# Devide into input and output

# %%
y = train["method"]
x = train.drop(['method','No'],axis=1)

# %% [markdown]
# training

# %%
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(x,y)

# %% [markdown]
# test for myself, I may need some help....

# %%
test = pd.read_csv("test.csv")
ans = tree.predict(test)
ans

# %% [markdown]
# We can find that the darker the color of the grid, the stronger the correlation between the two labels.

# %%
plt.figure(figsize = (20,8))
sns.heatmap(train.corr(), cmap = 'Blues', annot = True)


