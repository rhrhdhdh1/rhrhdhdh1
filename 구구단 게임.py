import random



for z in range (1 , 3):
    a = random.randint (1 , 9)
    b = random.randint (1 , 9)
    print(z, "번", a , "*", b, "는")
    y = a * b
    x = input("답 :")
    if int(x) == y:
        print("정답입니다")
    else:
        print("오답입니다.")


