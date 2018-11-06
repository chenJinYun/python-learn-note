
# coding: utf-8

# In[8]:


import pandas as pd
inputfile='D:/python note/练习数据代码/练习数据及代码/air_data.csv'
data=pd.read_csv(inputfile,encoding='utf-8')


# In[ ]:


explore=data.describe().T
print(explore)

