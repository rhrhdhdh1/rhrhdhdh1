# 아이디 비번이 같으면 break  다르면 컨티뉴


def login():

    x = list(range(0, 30))
    z = 0
    z = int(z)



    while True:

        print('--------------------------')

        w = int(input('1.회원가입 2. 로그인\n'))
        ww = 0

        if w == 1:
            a = None
            b = None
            c = None

            a = input('id:')
            b = input('password:')
            c = input('phone:')

            c1 = int(input('1번 등록 2번 취소\n'))

            if c1 == 0:
                continue
            elif c1 == 1:
                s = 0
                for q in range(z):
                    if a == x[q]['id']:
                        s = 10
                        print('중복된 id가 존재합니다.')
                        break
                if s == 10:
                    continue

                y = dict(zip(['id','password', 'phone'], [a, b, c]))

                x[z] = y
                print(x[z]['id'], '로 회원가입되셧습니다.')
                z = z + 1


        if w == 2:
            while True:
                id1 = input('아이디를 입력하세요.\n')
                pass1 = input('비밀번호를 입력하세요\n')
                for q1 in range(z):
                    if id1 == x[q1]['id'] and pass1 == x[q1]['password']:
                        ww = 10
                        print('로그인 되었습니다.')
                        break

                    else:
                        print('일치하지 않습니다.')
                        continue
                if ww == 10:
                    break
        if ww == 10:
            break
