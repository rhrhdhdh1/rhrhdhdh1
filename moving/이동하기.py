import moveclass

lo = moveclass.Point2D(100, 100)
lo1 = moveclass.Point2D(0, 0)
atype = 2
btype = 3
Time = 0
T = 0
T2 = 0
unit0 = moveclass.Unit(lo, atype)
p = lo
unit2 = moveclass.Unit(lo1, btype)
p1 = lo1
lenge1 = moveclass.lenge1(lo, lo1)
while True:
    Time += 1
    print()
    T += 1
    T2 += 1
    ctl = input('a. 0번유닛 조작 b. 1번유닛 조작 c. 둘다 조작  엔터는 통과 ')

    if ctl == 'a' or ctl == 'c':
        T = 0
        x = int(input('x좌표'))
        y = int(input('y좌표'))
        p = moveclass.Point2D(x, y)
        t = unit0.time(p)

    if ctl == 'b' or ctl == 'c':
        T2 = 0
        x1= int(input('x좌표'))
        y1 = int(input('y좌표'))
        p1 = moveclass.Point2D(x1, y1)
        t1 = unit2.time(p1)

    print('0번 유닛 위치는')
    unit0.move1(p, T)
    print('2번유닛 위치는')
    unit2.move1(p1, T2)

    c = lenge1.lenge()
    print(c)
