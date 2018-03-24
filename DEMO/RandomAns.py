RandAns = "9527"
OtherAns = "9487"

print(RandAns)  # print out the "9527"
print(OtherAns) # print out the "9487"

# it will return False
print(RandAns == OtherAns) # compare "9527" and "9487"

print(RandAns == RandAns)  # compare "9527" and "9487"

print("9527" == " 9527 ")  # ?? Guess that, False


import random
Num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

random.shuffle(Num)

print(Num)