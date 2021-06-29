

def ADD():  # 회원가입
    import json

    file = open('ADD.txt', 'r')
    x1 = file.read()
    file.close()
    x = json.loads(x1)
    www = 1
    a = None
    b = None
    c = None

    a = input('id:')
    b = input('password:')
    c = input('생년월일:')

    c1 = int(input('1번 등록 2번 취소\n'))

    if c1 == 0:
        print('취소되었습니다.')
    #    continue
    elif c1 == 1:

        for i in range(len(x)):
            if a == x[i]['ID']:
                print('중복된 ID가 존제합니다. 다시 가입해 주세요.')
                www = 10
                break
        if www == 1:
            y = dict(zip(['ID', 'Password', 'brith'], [a, b, c]))

            x.append(y)

            x2 = json.dumps(x)
            file1=open('ADD.txt','w')
            file1.write(x2)
            file1.close()
            print(a, '고객님 환영합니다.')

    print(x)


def Login():
    while True:
        import json
        ww = 0
        file = open('ADD.txt', 'r')
        x1 = file.read()
        file.close()
        x = json.loads(x1)

        a = input('아이디를 입력하세요.\n')
        b = input('비밀번호를 입력하세요\n')
        for q in range(len(x)):
            if a == x[q]['ID'] and b == x[q]['Password']:
                ww = int(10)
                break

        if ww == 10:
            print('로그인 되었습니다.')
            break
        else:
            print('일치하지 않습니다.')
    return ww ,a


def Login1():
    while True:
        ww = 0
        print('--------------------------')

        w = int(input('1.회원가입 2.로그인\n'))

        if w == 1:
            ADD()

        if w == 2:
            ww, a = Login()

        if ww == 10:
            break

    return a ,ww
