import random


a1, a2, a3, a4 = random.sample(range(1,5),4)
b1, b2, b3, b4 = input("상품을 입력후 ,를 눌러주세요").split(",")

for y in range(1,5):
    x = input("1-4중 1개를 선택하시오")
    x = int(x)
    if x == a1:
        print(b1)
    elif x == a2:
        print(b2)
    elif x == a3:
        print(b3)
    elif x == a4:
        print(b4)

