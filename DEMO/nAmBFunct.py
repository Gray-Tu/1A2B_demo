Ans = "9527"
Inp = "9287" # 之後可以用 input() 的數值

#n+m
Input_counter = 0 #計數器

for iChar in Inp:
    if iChar in Ans: # in 語句
        #當 iChar 存在於 Ans 中時，讓計數器 +1
        Input_counter = Input_counter + 1
        
print(Input_counter) #看結果，應該是 3

#n 
A_counter = 0

for x in range(4):

    AnsChar = Ans[x] # 用 index 方法取出內容
    InpChar = Inp[x] # x 會依照迴圈改變 
    
    if AnsChar == InpChar:
        A_counter = A_counter +1
        
print(A_counter) #結果應該是 2 

#end and output
n = A_counter
m = Input_counter - A_counter
print(n, "A", m, "B")