# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:31:14 2018

@author: CHENKI
"""

#print("hello world")
#print("hello python")

a='hello world'
b="kim"
c=1
d=[1]
e=1+2
#print(a)
#print(b)
#print(c)
#print(e)

#print(type(a))
#print(type(c))
#print(type(d))

"""
tuple:
    特点：不可变
"""

s1 = (2, 1.3, 'love', 5.6, 9, 12, False)       
s2 = (2, 'love',1.3)    
#print(s2)  
#print(type(s2))

#print(s1.count(2))
#print(s1[3])

"""
list:
    特点：可变，可以增删改，查询稍慢，，适合存储数组
"""

s3=["hello",'word',1,2]
s4=[[1,2,3,4],[2,3,4,5]]
s5=[5,4,2,1,4]
#print(s3)
#print(s3.count(1))
#print(s4[1][3])
#print(len(s4))
s3.append(5)
#sort没有返回值，不同类型不能排序
s5.sort()
#print(s5)
c=s5.sort()
#print(c) #none
#for item in s3:
    #print(item)
    
    
#包
#from collections import deque

#pip install packeage


#dict  键值对
    
dict1 = { 'x':42, 'y':3.14, 'z':7 }
#print(dict1)
#print(dict1["x"])
#print(dict1.has_key('x'))


#string

#str="heolloworld11111"
#print(str.index('s'))

if len(dict1) <0:
    print(len(dict1))
    if len(dict1)==3:
        print(True)

else:
    pass
    
    
#文件
#异常
#str="hello world"
#print(type(str))
try:
    f=open("D:/python note/python-code/text.txt","w")
    for i in range(0,10):
        f.write(str(i)+'meassage')
        f.write("\n")
    
except Exception as e:
    print(e)
    
finally:
    if(f!=None):
        f.close()
       
        
        
#函数
        
def test():
    print("function")
    
#传参
def testa(a):
    print(a)
    
def testRe(a):
    return a
#test()
#testa("can")
#print(testRe("hahahah"))
    
class Complex:
    def __init__(self,realpath,imagpart):
        self.r=realpath
        self.i=imagpart
        
    def addAge(self):
        print(self.r+self.i)
        
x=Complex(3.0,-4.5)
x.addAge()
#print(x.r,x.i)


#字符串的操作

#三引号

str1='''
    hello
    i
    am 
    kim
    '''
#print(str1=="hello i am kim")
    
    



































