import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from imblearn.combine import SMOTETomek
data = pd.read_csv('archive/glass.csv')
data.head()
data.shape
data.dtypes
data.isnull().sum()
data.describe()
data.corr()['Type'].sort_values()





datas_x = data.Type.value_counts().index.to_list()
datas_y = data.Type.value_counts().to_list()
suma = data.Type.value_counts().sum()
print(data.Type.value_counts())

list_color=['grey','black','orange','green','blue','red','red']
graph = plt.bar(datas_x, datas_y, color=list_color)
plt.title('Target data distribution')

i = 0

for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x+width/2,
             y+height*1.01,
             str(height)+" -> "+str(round(height/suma,2))+'%',
             ha='center',
             weight='bold')
    i+=1

plt.show()


filas=len(data.columns.to_list())
c=1
fig=plt.figure(figsize=(25,7*filas))
    
for i,j in enumerate(data.columns.to_list()):
    plt.subplot(filas,2, c)
    sns.distplot(data[j])
    c = c + 1
    
    plt.subplot(filas,2, c)
    ax1=sns.boxplot(x=data[j],palette="Blues",linewidth=1)
    c = c + 1

plt.show()



plt.figure(figsize=(10,6))
sns.heatmap(data.corr(), annot = True, cmap=None)
plt.show()
