

def passd():
    while True:

        b = input('password:')
        if len(b) >= 4:
            break

        else:
            print('비밀번호가 너무 짧습니다.')

    return b


def phoned():
    while True:
        d = input('휴대폰 번호를 구분자 없이 입력하시요.')

        if len(d) == 11:
            break
        else:
            print('휴대폰 번호가 11자리가 아닙니다.')

    return d


def IDD(x):
    while True:
        a = input('id:')
        www =2
        for i in range(len(x)):
            if a == x[i]['ID']:
                print('중복된 ID가 존제합니다. 다시 가입해 주세요.')
                www = 10
                break
        if www != 10:
            break
    return a

def Save(x):
    import json
    x2 = json.dumps(x)
    file1 = open('ADD.txt', 'w')
    file1.write(x2)
    file1.close()

def ADD():  # 회원가입
    import json
    import os.path
    isFile = os.path.isfile('ADD.txt')

    if isFile == False:
        newfile = [{'ID': 'root','Password':'1234','brith':'1234123','phone':'01036678711'}]
        newfile1 = json.dumps(newfile)
        with open('ADD.txt', 'w') as file3:
            file3.write(newfile1)


    file = open('ADD.txt', 'r')
    x1 = file.read()
    file.close()
    x = json.loads(x1)
    a = None
    b = None
    c = None
    c = None

    a = IDD(x)

    b = passd()

    c = input('생년월일:')

    d = phoned()


    c1 = int(input('1번 등록 2번 취소\n'))

    if c1 == 0:
        print('취소되었습니다.')
    #    continue
    elif c1 == 1:



        y = dict(zip(['ID', 'Password', 'brith','phone'], [a, b, c, d]))

        x.append(y)

        Save(x)

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
            break
        else:
            print('일치하지 않습니다.')
    return ww ,a ,q

def Modify1():
    z1 , z2, z3 =Login()
    import json
    file = open('ADD.txt', 'r')
    x1 = file.read()
    file.close()
    x = json.loads(x1)
    a = x[z3]['ID']
    b = x[z3]['Password']
    c = x[z3]['brith']
    d1 = x[z3]['phone']
    d2 = d1[0:3]
    d3 = d1[3:7]
    d4 = d1[7:12]
    print('ID:',a)
    print('Password:',b)
    print('brith :',c)
    print('phone', d2,'-', d3,'-', d4)

    while True:
        q = int(input('1.Id 수정 2.Password 수정 3.생일 수정 4.폰번호 수정 5.저장하고 나가기'))

        if q == 1:
            m = IDD(x)
            x[z3]['ID'] = m
            print('회원님의 ID가',m,'으로 변경되었습니다.')

        if q == 2:
            m = passd()
            x[z3]['Password'] = m
            print('회원님의 비밀번호가',m,'으로 변경되었습니다.')

        if q == 3:
            m = input('수정하실 생일을 입력하세요.')
            x[z3]['brith'] = m
            print('회원님의 생일이',m,'으로 변경되었습니다.')

        if q == 4:
            m = phoned()
            x[z3]['phone'] = m
            print('회원님의 폰번호가',m,'으로 변경되었습니다.')


        if q == 5:
            a = x[z3]['ID']
            b = x[z3]['Password']
            c = x[z3]['brith']
            d1 = x[z3]['phone']
            d2 = d1[0:3]
            d3 = d1[3:7]
            d4 = d1[7:12]
            print('ID:', a)
            print('Password:', b)
            print('brith :', c)
            print('phone', d2, '-', d3, '-', d4)

            Save(x)
            break

def Login1():
    while True:
        ww = 0
        print('--------------------------')

        w = int(input('1.회원가입 2.로그인 3.확인 및 수정\n'))

        if w == 1:
            ADD()

        if w == 2:
            ww, a = Login()
            print('로그인 되었습니다.')
        if w == 3:
            Modify1()

        if ww == 10:
            break

    return a ,ww
