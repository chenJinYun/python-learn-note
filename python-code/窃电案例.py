# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:03:12 2018

@author: CHENKI
"""

import pandas as pd
#1、读取数据
datafile="D:\python note\练习数据代码\练习数据及代码/model.xls"
data=pd.read_excel(datafile,"Sheet1")

testfile="D:\python note\练习数据代码\练习数据及代码/model_test.xls"
test_data=pd.read_excel(testfile,"Sheet1")
#2、数据格式化
data = data.as_matrix() #将表格转换为矩阵
#print(data)
p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集

trainx=train[:,:3].astype(int)
trainy=train[:,3].astype(int)
testx=test[:,:3].astype(int)
testy=test[:,3].astype(int)
#x=train.astype(int)
#y=test.astype(int)
#x=data.iloc[:,:3].as_matrix().astype(int)
#y=data.iloc[:,3].as_matrix().astype(int)

#test_x=test_data.iloc[:,:3].as_matrix().astype(int)
#test_y=test_data.iloc[:,3].as_matrix().astype(int)

#3.决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC() #默认是GINI，即CART  criterion='entropy'
dtc.fit(trainx,trainy)
print(dtc.score(trainx,trainy)) #0.9450171821305842
#print(dtc.score(train,test)) #0.9
#4、建模


#5、调优

from sklearn import grid_search
parameters = {'criterion':('entropy', 'gini'), 'max_depth':[1,2,3,4,6,9,10,50,70, 100]}
clf = grid_search.GridSearchCV(dtc, parameters)
clf.fit(trainx,trainy)
print(clf.best_params_) #{'criterion': 'entropy', 'max_depth': 3}
print(clf.best_score_) #0.896551724137931
dtc1=DTC(criterion= 'entropy', max_depth=3)
dtc1.fit(trainx,trainy)
print(dtc1.score(testx,testy)) #0.9491525423728814


#换模型，数据，特征不换 贝叶斯
from sklearn.naive_bayes import MultinomialNB #适合做文本
from sklearn.naive_bayes import BernoulliNB #适合做true and false 取特征值
from sklearn.naive_bayes import GaussianNB #适合做特征是连续的

bayes=MultinomialNB()
bayes.fit(trainx,trainy)
print(bayes.score(testx,testy)) #0.9661016949152542

bayes1=BernoulliNB()
bayes1.fit(trainx,trainy)
print(bayes1.score(testx,testy)) #0.9661016949152542

bayes2=GaussianNB()
bayes2.fit(trainx,trainy)
print(bayes2.score(testx,testy)) #0.9830508474576272










































