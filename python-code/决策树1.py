# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:21:57 2018

@author: CHENKI
"""

from sklearn import datasets #导入数据集



iris=datasets.load_iris() #加载数据集 

#print(type(iris))
#shape看数据集大小
#print(iris.data.shape)#查看数据集大小

from sklearn import svm #导入SVM模型
clf=svm.LinearSVC() #建立线性SVM模型
clf.fit(iris.data,iris.target) #用数据训练模型
#print(iris.target)
#print(type(iris.data)) #ndarray
#print(clf.predict([[5.0,3.6,1.3,0.25]])) #训练好模型后，用新数据进行预测
#clf.coef_ #查看训练好的模型的参数
#print(clf.coef_)

#print(clf)





#决策树实现
from sklearn.tree import DecisionTreeClassifier as DTC

dtc=DTC() #默认是GINI，即CART  criterion='entropy'
dtc.fit(iris.data,iris.target)
print(dtc.predict(iris.data))






























