
x = list(range(0, 30))
z = 0
z = int(z)



while True:

    print('--------------------------')

    w = int(input('1입력 2인쇄 3검색 4수정 0취소\n'))


    if w == 1:
        a = None
        b = None
        c = None

        a = input('이름:')
        b = input('번호:')
        c = input('생일:')

        c1 = int(input('1번 등록 2번 취소\n'))

        if c1 == 0:
            continue
        elif c1 == 1:

            y = dict(zip(['name','phone', 'brith'], [a, b, c]))
            print(y,'가', z+1,'번으로저장되었습니다.')


            x[z] = y
            z = z + 1


    if w == 2:
        for q in range(z):
            print(q+1,'번',x[q])


    if w == 3:
        w1 = int(input ('1이름으로 검색 2폰번호으로 검색 3생일으로 검색 4리스트번호로 검색\n'))

        if w1 == 0:
            continue

        if w1 == 1:
            w2 = input ('이름을 입력하세요.\n')


            for z1 in range(z):
                if w2 == x[z1]['name']:
                    print(z1,'번',x[z1])


        if w1 == 2:
            w3 = input('번호를 입력하세요.\n')

            for z2 in range(z):
                if w3 == x[z2]['phone']:
                    print(z2,'번',x[z2])


        if w1 == 3:
            w4 = input('폰번호를 입력하세요.\n')

            for z3 in range(z):
                if w4 == x[z3]['phone']:
                    print(z3,'번',x[z3])

        if w1 == 4:
            w5 = int(input('리스트 번호를 입력하세요.\n'))

            if w5 <= z :
                print(w5,'번',x[w5-1])

            else:
                print('해당번호는 비어있습니다.')

    if w == 4:
        d1 = int(input('수정을 원하시는 번호를 입력하세요. 0취소\n'))
        if d1 == 0:
            continue
        print(d1,'번',x[d1-1])

        d2 = int(input('1이름수정 2번호수정 3생일수정 0취소 \n'))
        if d2 == 0:
            continue

        if d2 == 1:
            d3 = 'name'
        elif d2 == 2:
            d3 = 'phone'
        elif d2 == 2:
            d3 = 'brith'


        d4 = input(' \'수정할 내용\' 다음양식으로 적으세요.\n')

        c2 = int(input('1번 수정 0번 취소'))

        if c2 == 0:
            continue

        if c2 == 1:

            x[d1-1][d3] = d4
            print(d1-1,'번',x[d1-1])


    else :
        continue

