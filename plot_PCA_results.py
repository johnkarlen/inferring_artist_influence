from matplotlib import pyplot as plt
import numpy as np

import re

labels_file = open('labels.txt', 'r')
labels = [str(line.split(',')[0][:-1]) for line in labels_file.readlines()]
painters = [l.split(" : ")[0] for l in labels]
print(painters)

t_X = np.load("t_X.npy")
print(len(labels))
print(t_X.shape)

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
 
# Create dataframe
df = pd.DataFrame({
'x': t_X[::2,0],
'y': t_X[::2,1],
'group': labels[::2],
'painter': painters[::2]
})

#df = df.drop_duplicates('group')
p1=sns.regplot(data=df, x="x", y="y", fit_reg=False, scatter_kws={'s':2})
#p1=sns.lmplot( x="x", y="y", data=df, fit_reg=False, hue='painter', legend=False)
 
# add annotations one by one with a loop
for line in range(0,df.shape[0]):
     p1.text(df.x[line]+0.2, df.y[line], df.group[line], fontsize=10)# horizontalalignment='left', size='medium', color='black', weight='semibold')

plt.xlabel('PCA component 1')
plt.ylabel('PCA component 2')
plt.show()

