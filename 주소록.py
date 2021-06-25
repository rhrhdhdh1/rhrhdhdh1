
addlist = list(range(0, 4))
z = 0
z = int(z)


while z != 4:
    addlist[z] = list(range(0,10))
    x = 0
    x = int(x)
    print(z)
    while x != 10:

        x = x + 1

        print(addlist[z])
        a = None
        b = None
        c = None

        a = input('이름:')
        b = input('지역:')
        c = input('번호:')

        y = [a ,b, c]

        addlist[z][x-1] = y
        print(addlist[z])
        print(addlist)

    z = z + 1