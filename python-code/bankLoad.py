# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:20:19 2018

@author: CHENKI
"""

import pandas as pd

inputfile='D:\python note\练习数据代码\练习数据及代码/bankloan.xls'

#1、读取数据
data=pd.read_excel(inputfile,'bankloan')
data=data.as_matrix() #将表格转换为矩阵

#2、数据格式化
p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集

#抽取一部分作为训练数据，一部分为测试数据
trainx=train[:,:8].astype(float)
trainy=train[:,8].astype(float)

testx=test[:,:8].astype(float)
testy=test[:,8].astype(float)
#3、决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC() #默认是GINI，即CART  criterion='entropy'
dtc.fit(trainx,trainy)
print('决策树',dtc.score(testx,testy)) #0.75



#5、调优

from sklearn import grid_search
parameters = {'criterion':('entropy', 'gini'), 'max_depth':[1,2,3,4,6,9,10,50,70, 100]}
clf = grid_search.GridSearchCV(dtc, parameters)
clf.fit(trainx,trainy)
#print(clf.best_params_) #{'criterion': 'entropy', 'max_depth': 4}
#print(clf.best_score_) #0.7535714285714286
dtc1=DTC(criterion= 'gini', max_depth=2)
dtc1.fit(trainx,trainy)
print('决策树调优',dtc1.score(testx,testy)) #0.7714285714285715


#随机森林
from sklearn.ensemble import RandomForestClassifier
randomForest=RandomForestClassifier(max_depth=8)
randomForest.fit(trainx,trainy)
print('随机森林',randomForest.score(testx,testy)) #0.8285714285714286

#增强模型，有权重
from sklearn.ensemble import AdaBoostClassifier
adaBoost=AdaBoostClassifier()
adaBoost.fit(trainx,trainy)
print('增强模型',adaBoost.score(testx,testy)) #0.8142857142857143

#逻辑回归
from sklearn.linear_model import LogisticRegression as LR
lr=LR(max_iter=5)
lr.fit(trainx,trainy)
print('逻辑回归',lr.score(testx,testy)) #0.8357142857142857

