# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:48:57 2018

@author: CHENKI
"""

import pandas as pd
#1、读取数据
datafile="D:\python note\练习数据代码\练习数据及代码/model.xls"
data=pd.read_excel(datafile,"Sheet1")
#2、数据格式化
data = data.as_matrix() #将表格转换为矩阵
p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集

#抽取一部分作为训练数据，一部分为测试数据
trainx=train[:,:3].astype(int)
trainy=train[:,3].astype(int)

testx=test[:,:3].astype(int)
testy=test[:,3].astype(int)

#3.决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC() #默认是GINI，即CART  criterion='entropy'
dtc.fit(trainx,trainy)
#print(dtc.score(trainx,trainy)) #0.9439655172413793

#随机森林
from sklearn.ensemble import RandomForestClassifier
randomForest=RandomForestClassifier()
randomForest.fit(trainx,trainy)
#print(randomForest.score(trainx,trainy)) #0.9439655172413793
#print(randomForest.feature_importances_) #[0.52221953 0.13720082 0.34057964] 选出特征值的重要性

#增强模型，有权重
from sklearn.ensemble import AdaBoostClassifier
adaBoost=AdaBoostClassifier(n_estimators=11)
adaBoost.fit(trainx,trainy)
#print(adaBoost.score(trainx,trainy)) #0.9267241379310345

#逻辑回归
from sklearn.linear_model import LogisticRegression as LR
lr=LR(max_iter=5)
lr.fit(trainx,trainy)
print(lr.score(trainx,trainy)) #0.9008620689655172



















