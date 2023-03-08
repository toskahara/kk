'''
Created on 2023/01/31

@author: class
'''

#coding:utf-8
import random

ax=[""] *4


for i in range(4):
    ax[i]=str(random.randint(0,9))
    
print(ax)   

import re

isok = False
while isok == False:
    myinput = input("数字を入力してください")
    if not re.match(r"^\d\d\d\d$", myinput):
        print("4桁の数字を入力して下さい")
    else:
        print("Ok")
        isok = True
    
hit = 0
blow = 0
for j in range(4):
    if ax[j] == myinput[j]:
        hit=hit+1
        
print(hit)

for j in range(4):
    for i in range(4):
        if i==j:            # 同じ場所は、、スキップ 
            continue
        
        if ax[i] == myinput[j] and ax[j] != myinput[j]:
            blow=blow + 1
            break
        
print(blow)
              
    
    


