ww = 0
x = [{'ID':'root','Password':'1234', 'brith':'121212'}]
def ADD(): # 회원가입
    www= 1
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
            y = dict(zip(['ID','Password', 'brith'], [a, b, c]))

            x.append(y)

            print(a,'고객님 환영합니다.')
    print(x)

def Login():

    while True:
        ww = 0
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
    return ww

def Login1():

    while True:
        ww = 0
        print('--------------------------')

        w = int(input('1.회원가입 2. 로그인\n'))


        if w == 1:
            ADD()

        if w == 2:
            ww = Login()

        if ww == 10:
            break




Login1()
