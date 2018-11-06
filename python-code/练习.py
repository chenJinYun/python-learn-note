# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:00:02 2018

@author: CHENKI
"""

import pandas as pd

datafile='D:/AllElectronics.csv'
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.cluster import KMeans

data = pd.read_csv(datafile,index_col = u'RID')
print(type(data))


# In[12]:


data[data == u'youth']=1
data[data == u'middle_aged']=2
data[data == u'senior']=3
data[data == u'high']=1
data[data == u'medium']=2
data[data == u'low']=3
data[data == u'yes']=1
data[data == u'no']=0
data[data == u'excellent']=1
data[data == u'fair']=0
print(data)

p = 0.8
train = data[:int(len(data) * p)]
test = data[int(len(data) * p):]
xtrain = train.iloc[:,:4].as_matrix().astype(int)
ytrain = train.iloc[:,4].as_matrix().astype(int)

xtest = test.iloc[:,:4].as_matrix().astype(int)
ytest = test.iloc[:,4].as_matrix().astype(int)


# In[13]:


dtc=DTC()
dtc.fit(xtrain,ytrain)
print(dtc.score(xtest,ytest))


# In[10]:


k=3
kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型

print(kmodel.cluster_centers_) #查看聚类中心
print(kmodel.labels_) #查看各样本对应的类别












