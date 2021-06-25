x = 0

addlist = list(range(1 ,100))


while x != 100:
    x = int(x)
    x = x + 1

    a = None
    b = None
    c = None

    a = input("이름을 입력하세요.")
    b = input('지역을 입력하세요.')
    c = input('번호를 입력하세요.')

    y = [a ,b ,c]
    addlist[x] = y
    print(addlist)


