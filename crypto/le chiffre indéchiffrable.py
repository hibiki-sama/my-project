# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:16:10 2019

@author: 55416
"""
import re
#列表去重函数
def simplifiy_list(alist):
    set_list=set(alist)
    alist=[]
    for i in set_list:
        alist.append(i)
    #print("The simplified list is:",alist)
    return alist 
#定义列表元素求和函数
def add_the_list(alist):
    the_sum=0
    for i in range(len(alist)):
        the_sum=alist[i]+the_sum
    return the_sum
#test_list=[1,2,3,4,5.1]
#t1=add_the_list(test_list)
#print("t1 is :",t1) 
def sub_stdfre(fre):
    return abs(fre-0.06549669949999998)
def zip_flist(fre,n):
    return (n,fre)
def all_lower(c):
    return c.lower()
flist=[]
ave_flist=[]
len_list=[]
result=[]
res=[]
initial_text=input("Please input text:")#读入文本
simplified_text=re.sub('[^a-zA-Z]','',initial_text)#去除非英文字母字符
letter_cnt=len(simplified_text)#英文字母总个数
simp_text=map(all_lower,simplified_text)#都换成小写字母
text_list=list(simp_text)#将简化的文本列表化
for key_len in range(2,50):   
    len_list.append(key_len)
    for i in range(key_len):
        templist=text_list[i::key_len]
        #print(templist)
        sqcnt_list=[]
        temp_len=len(templist)#分组字母个数
        once_list=simplifiy_list(templist)#对当前分组去重复
        for letter in range(len(once_list)):
            #对于非重复列表中的每一个字母，查找它在templist出现了多少次
            cnt=templist.count(once_list[letter])#字母在templist出现的次数
            sqcnt=cnt*(cnt-1)#我们假设文本数量足够大，不会出现cnt==1的情况
            sqcnt_list.append(sqcnt)#存放的都是sqcnt
        flist.append(add_the_list(sqcnt_list)/(temp_len*(temp_len-1)))
    ave_fre=add_the_list(flist)/len(flist)
    ave_flist.append(ave_fre)
res=list(zip(len_list,(list(map(sub_stdfre,ave_flist)))))
result=sorted(res, key=lambda x:x[1])
print("最有可能的前十个密钥长度及其对应频率和0.065差值为：")
for i in range(10):
    print(result[i])

# 根据密钥长度将密文分组 
def makelist(text,length): 
    textarray = []
    row = []
    index = 0
    for ch in text:
        row.append(ch)
        index += 1
        if index % length ==0:
            textarray.append(row)
            row = []
    return textarray
#标准的频率表
freq=[0.08167	,0.01492,	0.02782,	0.04253,	0.12702,	0.02228,			0.02015,0.06094	,0.06966	,0.00153	,0.00772	,0.04025,	0.02406,	0.06749	, 0.07507	,0.01929	,0.00095	,0.05987	,0.06327,	0.09056,	0.02758,
	0.00978	,0.0236	,0.0015	,0.01974	,0.00074]
# 统计字母频度
def f_list(lis): 
    li = []
    alphabet = [chr(i) for i in range(97,123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count+=1
        li.append(count/len(lis))
    return li

def MyKey(text,length): 
    key = [] 
    array =makelist(text,length)
    for i in range(length):
        flist = f_list([row[i] for row in array]) 
        multi = [] 
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += freq[k]*flist[k]
            multi.append(Sum)
            flist = flist[1:]+flist[:1]
        n = 100
        ch = ''
        for j in range(len(multi)):
             if abs(multi[j] -0.065)<n: 
                 n = abs(multi[j] -0.065)
                 ch = chr(j+97)
        key.append(ch)
    return key    

k=MyKey(simplified_text,10)
print("猜测的密钥为：",k)


