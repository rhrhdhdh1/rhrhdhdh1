class UPsave:

    def __init__(self, savefile ):
        self.savefile = savefile

    def Read(self):
        import json
        import os.path

        isFile = os.path.isfile(self.savefile)

        if isFile == False:
            newfile = [{'ID': 'root', 'Password': '1234', 'brith': '1234123', 'phone': '01036678711'}]
            newfile1 = json.dumps(newfile)
            with open(self.savefile, 'w') as file3:
                file3.write(newfile1)

        file = open(self.savefile, 'r')
        x1 = file.read()
        file.close()
        x = json.loads(x1)

        return x


    def Save(self,x):
        import json
        x2 = json.dumps(x)
        file1 = open(self.savefile, 'w')
        file1.write(x2)
        file1.close()

    def Save1(self,x1 , z1):
        x = x1
        z = z1

        c1 = int(input('1번 등록 2번 취소\n'))

        if c1 == 0:
            print('취소되었습니다.')

        elif c1 == 1:

            y = dict(zip(['ID', 'Password', 'brith', 'phone'], z))

            x.append(y)

            self.Save(x)


    def IDD(self, x1):

        x = x1
        print(x)
        while True:
            a = self.ID()
            www = 2
            for i in range(len(x)):
                if a == x[i]['ID']:
                    print('중복된 ID가 존제합니다. 다시 가입해 주세요.')
                    www = 10
                    break
            if www != 10:
                break
        return a


    def ID(self):
        while True:
            a = input('id:')

            if len(a) > 10:
                print('ID가 너무 깁니다.')

            elif len(a) < 3:
                print('ID가 너무 짧습니다.')
            else:
                break

        return a

    def PASD(self):
        while True:

            b = input('password:')
            if len(b) >= 4:
                break

            else:
                print('비밀번호가 너무 짧습니다.')

        return b

    def Brith(self):
        while True:

            c = input('생일을 입력하세요. ex)19921207')
            if len(c) == 8:
                break

            else:
                print('생일이 8자리는 아닙니다.')

        return c

    def Phone(self):
        while True:
            d = input('휴대폰 번호를 구분자 없이 입력하시요.')

            if len(d) == 11:
                break
            else:
                print('휴대폰 번호가 11자리가 아닙니다.')

        return d
    def login1(self, x1):
        ww = 1
        while True:
            x = x1
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
        return a, ww ,q

    def modprint(self, x, q):
        a = x[q]['ID']
        b = x[q]['Password']
        c = x[q]['brith']
        d1 = x[q]['phone']
        d2 = d1[0:3]
        d3 = d1[3:7]
        d4 = d1[7:12]
        print ('ID:', a)
        print ('Password:', b)
        print ('brith :', c)
        print ('phone', d2, '-', d3, '-', d4)


    def modify1(self,x ,z3):
        while True:
            q = int(input('1.Id 수정 2.Password 수정 3.생일 수정 4.폰번호 수정 5.저장하고 나가기'))

            if q == 1:
                m = self.IDD()
                x[z3]['ID'] = m
                print('회원님의 ID가',m,'으로 변경되었습니다.')

            if q == 2:
                m = self.PASD()
                x[z3]['Password'] = m
                print('회원님의 비밀번호가',m,'으로 변경되었습니다.')

            if q == 3:
                m = self.Brith()
                x[z3]['brith'] = m
                print('회원님의 생일이',m,'으로 변경되었습니다.')

            if q == 4:
                m = self.Phone()
                x[z3]['phone'] = m
                print('회원님의 폰번호가',m,'으로 변경되었습니다.')

            if q == 5:
                self.modprint(x , z3)
                self.Save(x)
                break





    def add1(self):
        x = self.Read()
        a = self.IDD(x)
        b = self.PASD()
        c = self.Brith()
        d = self.Phone()

        z =[a, b, c, d]

        self.Save1(x ,z)


    def login(self):
        x = self.Read()
        a, ww, q=self.login1(x)
        return a, ww

    def modify(self):
        x = self.Read()
        a, ww, q =self.login1(x)
        self.modprint(x, q)
        self.modify1(x, q)

