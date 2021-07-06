
def login(x):
    import upsaves
    b = upsaves.UPsave(x)

    while True:
        ww = 0
        print ('--------------------------')

        w = int (input ('1.회원가입 2.로그인 3.확인 및 수정\n'))

        if w == 1:
            b.add1()

        if w == 2:
            a, ww =b.login()
            print ('로그인 되었습니다.')
        if w == 3:
            b.modify()


        if ww == 10:
            break

    return a , ww

