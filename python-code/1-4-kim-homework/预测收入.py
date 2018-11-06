
# coding: utf-8

# In[140]:


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[141]:


# 从csv文件中读取数据
def get_data(file_name):
    data=pd.read_excel(file_name,'bankloan',encoding ='utf-8')
    X_parameter=[]
    Y_parameter=[]
    for single_square_feet,age,workage,single_price_value in zip(data['年龄'],data['教育'],data['工龄'],data['收入']):
        X_parameter.append([float(single_square_feet),float(age),float(workage)])
        Y_parameter.append(float(single_price_value))
    return X_parameter,Y_parameter


# In[142]:


# 线性回归分析
def linear_model_main(X_parameter,Y_parameter,predict_square_feet):
    # 1. 构造回归对象
    regr=LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    #y=regr.predict(X_parameter)
    # 2. 获取预测值
    predict_outcome=regr.predict(predict_square_feet)
    # 3. 构造返回字典
    predictions={}
    # 3.1 截距值
    predictions['intercept']=regr.intercept_
    # 3.2 回归系数（斜率值
    predictions['coefficient']=regr.coef_
    # 3.3 预测值
    predictions['predict_value']=predict_outcome
    #print(mean_squared_error(Y_parameter, y))
    # Explained variance score: 1 is perfect prediction
    #print(r2_score(Y_parameter, y))
    return predictions


# In[149]:


def show_linear_line(X_parameter,Y_parameter):
    # 1. 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    
    # 2. 绘出已知数据散点图
    plt.scatter(X_parameter,Y_parameter,color = 'blue')
    
    # 3. 绘出预测直线
    plt.plot(X_parameter,regr.predict(X_parameter),color = 'red',linewidth = 10)
    plt.title('收入预测')
    plt.xlabel('square feet')
    plt.ylabel('收入')
    plt.show()


# In[150]:


def main():
    # 1. 读取数据
    X,Y = get_data('D:/python note/bankloan.xls')
    # print(X,Y)
    # 2. 获取预测值，在这里我们预测700平方英尺大小的房子的房价
    predict_square_feet = [[41,3,17]]
    result = linear_model_main(X,Y,predict_square_feet)
    for key,value in result.items():
        print(key,value)
    # 3. 绘图
    show_linear_line(X,Y)
if __name__ == '__main__':
    main()

