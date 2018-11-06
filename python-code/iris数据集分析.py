# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:50:16 2018

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
clf.coef_ #查看训练好的模型的参数
#print(clf.coef_)

#print(clf)


print("124"=="124")