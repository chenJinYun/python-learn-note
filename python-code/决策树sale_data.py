# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:45:18 2018

@author: CHENKI
"""

#1.读入数据

import pandas as pd

inputfile='D:/python note/练习数据代码/练习数据及代码/sales_data.xls'

testPath='D:/python note/练习数据代码/练习数据及代码/sales_data_text.xls'

data=pd.read_excel(inputfile,'sales_data',index_col=u'序号')
textData=pd.read_excel(testPath,'sales_data',index_col=u'序号')

#print(data)
#print(type(data)) #<class 'pandas.core.frame.DataFrame'>

#2.数据清洗
#print(data[data==u'好'])
data[data==u'youth']=1
data[data==u'middle_aged']=1
data[data==u'high']=1
data[data==u'medium']=1
data[data==u'yes']=1
data[data==u'excellent']=1
data[data!=1]=0

textData[textData==u'好']=1
textData[textData==u'是']=1
textData[textData==u'高']=1
textData[textData!=1]=0

#print(data)

#3.数据格式化 select x,y transfor x,y=matrix(ndarray)
x=data.iloc[:,:3].as_matrix().astype(int)
y=data.iloc[:,3].as_matrix().astype(int)

test_x=textData.iloc[:,:3].as_matrix().astype(int)
test_y=textData.iloc[:,3].as_matrix().astype(int)

#print(x)
#print(y)

#4.决策树
from sklearn.tree import DecisionTreeClassifier as DTC

dtc=DTC() #默认是GINI，即CART  criterion='entropy'
dtc.fit(x,y)
#print(dtc.score(x,y))

#print(dtc.score(test_x,test_y))

#调优
from sklearn import grid_search
parameters = {'criterion':('entropy', 'gini'), 'max_depth':[1, 10]}
clf = grid_search.GridSearchCV(dtc, parameters)
clf.fit(x,y)
#print(clf.best_params_)
dtc1=DTC(criterion= 'entropy', max_depth=9)
dtc1.fit(x,y)
print(dtc1.score(test_x,test_y))

#换模型，数据，特征不换 贝叶斯
from sklearn.naive_bayes import MultinomialNB #适合做文本
from sklearn.naive_bayes import BernoulliNB #适合做true and false 取特征值
from sklearn.naive_bayes import GaussianNB #适合做特征是连续的

bayes=MultinomialNB()
bayes.fit(x,y)
print(bayes.score(test_x,test_y))

bayes1=BernoulliNB()
bayes1.fit(x,y)
print(bayes1.score(test_x,test_y))

bayes2=GaussianNB()
bayes2.fit(x,y)
print(bayes2.score(test_x,test_y))

































