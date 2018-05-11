
# -*- coding: utf-8 -*-
#1A2B
#   author: Gray
#   version: 1.1
#   date: 20180511
'''
    規則
    輸入錯誤則提供提示
        nA: 有 n 個數字存在答案中並同時位置正確。
        mB: 有 m 個數字存在答案中但位置錯誤。
'''

import random
import unicodedata

def getAns():
    """
        產生一組隨機，且不重複的四個數字
    """
    oriList = list('0123456789')
    random.shuffle(oriList)
    AnsList = oriList[:4]
    return AnsList

def is_number(string_A):
    """
        檢查 string_A 是否由數字組成
        ref: http://www.runoob.com/python3/python3-check-is-number.html
    """
    try:
        float(string_A)
        return True
    except ValueError:
        pass
        
    try:
        # unicodedata
        unicodedata.numeric(string_A)
        return True
    except (TypeError, ValueError):
        pass
       
    return False
 

def is_repeat(string_A):
    """
        檢查數字是否重複
    """
    if len(list(string_A)) != len(set(list(string_A))):
        return True
    else:
        return False
 
 
    
def InputCheck():
    """
        讓使用者輸入，並檢查是否為不重複的四個數字
        若不合法，要求在輸入一次。
        
    Return
        a list
    """
    UserInput = input("請輸入四個數字: ").strip()  #.strip()清除頭尾空白字元
    
    #check 長度
    if len(UserInput) != 4:
        print("Error: 長度錯誤")
        return InputCheck()  #遞迴檢查
    
    else:
        #check 數字
        if is_number(UserInput): 
            #check 重複
            if is_repeat(UserInput):
                print("Error: 數字有重複")
                return InputCheck()  #遞迴檢查
            else:
                return list(UserInput)
        else:
            print("Error: 輸入並非數字")
            return InputCheck()  #遞迴檢查
        
            
    
    return list(UserInput)
    
    
def AnsCompare(A_list, B_list):
    """
        傳回 nAmB
        輸入錯誤則提供提示
            nA: 有 n 個數字存在答案中並同時位置正確。
            mB: 有 m 個數字存在答案中但位置錯誤。
    """
    
    #先統計有多少數字被猜到
    right_number = 0
    for b_number in B_list:
        if b_number in A_list:
            right_number += 1
            
    right_site = 0
    #再統計正確位置的數字有多少
    for site in range(4):
        if A_list[site] == B_list[site]:
            right_site += 1
    
    #回傳 nAmB
    return "{0}A{1}B".format(right_site, right_number - right_site)
    
    
if __name__ == "__main__":
    randAns = getAns()  #亂數產生答案 #list
    
    #對輸入進行檢查與轉換
    UserInput = InputCheck() #list      
    #print(randAns, UserInput)
    
    K = 5
    while(K):
        K -= 1
        if randAns == UserInput:
            print("恭喜答對："+" ".join(randAns))
        else:
            
            print(AnsCompare(UserInput,randAns),"剩餘次數: {0}".format(K+1))
            UserInput = InputCheck()
    
    if randAns == UserInput:
        print("恭喜答對："+" ".join(randAns))        
    else:
        print("GG 答案:{0}".format("".join(randAns)))
