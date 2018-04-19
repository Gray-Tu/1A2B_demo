MyInput = input("試試 input:")

print("剛剛輸入的字串是"+MyInput)

#辦斷數字

if MyInput.isdigit():
    print("Yes, 是數字\n輸入正確，棒棒")
    
else:
    print("No, 不是數字，回去重寫")

#判斷位數
if len(MyInput) == 4:
    print("長度為 4 ，Great")
    
else:
    print("Error: 長度錯誤")
    
#判斷重複
Flag = 0  #準備一個旗子
#第一次比較
x = 0
for y in range(1, len(MyInput)): #由第二個位開始比較
    if MyInput[x] == MyInput[y]:
        print("有重複")
        Flag = 1  #插個旗子，表示有遇到重複

x = 1
for y in range(2, len(MyInput)): #由第三個位開始比較
    if MyInput[x] == MyInput[y]:
        print("有重複")
        Flag = 1  #插個旗子，表示有遇到重複

x = 2
for y in range(3, len(MyInput)): #由第四個位開始比較
    if MyInput[x] == MyInput[y]:
        print("有重複")
        Flag = 1  #插個旗子，表示有遇到重複

if Flag == 0:
    print("沒重複")
else:
    print("回去重寫")