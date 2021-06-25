import random

x = None
z = 0
s = None

while True:
    print("다음 수를 곱하여 적으시오. 기회는 총 5회이며 총 3문제 입니다.")
    z = 0
    for q in range (1 , 4):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = a * b
        print(a,b,c)

        while x != c:
            f = 5 - z
            print("life %d" % f)
            print(q,"번 문제",a, "x", b, end='')
            x = input("=")
            x = int(x)


            if x != c:
                z = z + 1
                print("오답입니다.")
            else:
                print("정답입니다.")
            if z > 4:
                break
        if z > 4:
            break
    if f >1:
        print(" 클리어!!! 남은 life%s" %f)
    else:
        print("fail")

    s = input ("게임의 종료를 원하시면 0을 입력하세요.")
    s = int(s)
    print (s)
    if s == 0:
        break
print("감사합니다")

