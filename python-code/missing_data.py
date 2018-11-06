# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:20:31 2018

@author: CHENKI
"""

import pandas as pd
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile="D:/python note/练习数据代码/练习数据及代码/missing_data.xls"
outputfile="D:/python note/练习数据代码/练习数据及代码/missing_data_process.xls"

#1.数据读取
data=pd.read_excel(inputfile,'Sheet1',header=None)
#print(data)

#2、数据填充
def ployinterp_column(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]
    return lagrange(y.index,list(y))(n)

for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j]=ployinterp_column(data[i],j)

data.to_excel(outputfile,header=None,index=False)






















    