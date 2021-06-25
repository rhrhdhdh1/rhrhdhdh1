import random
import 로그인

로그인.login()


z = None
x = input ("인원수를 입력하시오")
x = int (x)

a = random.sample(range(1,x+1),x)
#print(a)

b = list(range(1,x+1))
#print(b)
for d in range (0 , x):
    b[d] = input("상품을 입력하세요")
print(b)
y = input("수를 선택하세요")
y = int(y)


while z != 1:
    for q in range (0 , x):
        if y == a[q]:
            print(b[q])
    z = input ("끝내고 싶으면 1 을 입력하세요")
    z = int(z)
