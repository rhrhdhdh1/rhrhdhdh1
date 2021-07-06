class boardclass1:
    def __init__(self, savefile):
        self.savefile = savefile


    def save(self, x):
        import json
        x2 = json.dumps(x)
        with open(self.savefile, 'w') as file1:
            file1.write(x2)

    def read(self):
        import json
        import os.path
        isFile = os.path.isfile (self.savefile)

        if isFile == False:
            newfile = list()
            newfile1 = json.dumps (newfile)
            with open (self.savefile, 'w') as file3:
                file3.write (newfile1)

        with open (self.savefile, 'r') as file:
            x1 = file.read ()
        x = json.loads (x1)

        return x



    def boardread1(self, x):
        x = x
        for i in range(len(x)):
            a = i
            b = x[i]['Title']
            c = x[i]['Id']
            print('{}번 제목:{} 작성자 {}'.format(a, b, c))

    def boardread2(self, x):
        x3 = int(input ('읽기를 원하시는 번호를 입력하세요'))
        a1 = x3
        b1 = x[x3]['Title']
        c1 = x[x3]['Id']
        d1 = x[x3]['Contents']
        print('--------------------------------------------------')
        print('{}번 제목 :{}           작성자:{}'.format (a1, b1, c1))
        print('                  내용')
        print(d1)
        print('---------------------------------------------------')
        self.boardread1(x)

    def modify1(self, x):
        w = 1
        while True:
            y = int(input('수정을 원하는 글의 번호를 입력하세요.'))
            z = input('수정을 원하는 글의 비밀번호를 입력하세요.')

            if x[y]['Password'] == z:
                w = 10
                break
            else:
                print('글 번호와 비밀번호가 일치가히 않습니다.')
            r = int(input('1. 다시시도  2. 끝내기'))

            if r == 2:
                break
        return w, y

    def modify2(self, x, y, y1):
        y0 = ['Title', 'Contents']
        x2 = y0[y1 - 1]
        z2 = x[y][x2]
        z1 = input('수정할 내용을 입력하세요')
        x[y][x2] = z1
        print(z2, '에서', x[y][x2], '로 변경되었습니다.')
        return x

    def find(self,x):
        y = int (input ('1.Id로 검색\n2.Contents로 검색\n3.Title로 검색\n'))
        y1 = ['Id', 'Contents', 'Title']
        x1 = y1[y-1]
        z = input('검색 내용을 입력하세요\n')
        print(z, '로 검색한 결과')
        qw = 1
        for i in range(len(x)):
            if x[i][x1].find(z) != -1:
                a1 = i
                b1 = x[i]['Title']
                c1 = x[i]['Id']
                d1 = x[i]['Contents']
                print('--------------------------------------------------')
                print('{}번 제목 :{}           작성자:{}'.format(a1, b1, c1))
                print('                  내용')
                print(d1)
                print('---------------------------------------------------')
                qw = 10
        if qw != 10:
            print(z, '로 검색된 내용이 없습니다.')
        return qw



    def boardwrite (self, ID):

        x = self.read ()

        a = None
        b = None
        c = None
        d = None
        a = input ('제목을 입력하세요.')
        b = input ('내용을 입력하세요.')
        c = ID
        d = input ('글 비밀번호를 입력하세요.')
        y = dict (zip (['Title', 'Contents', 'Id', 'Password'], [a, b, c, d]))
        x.append (y)

        self.save(x)

    def boardread(self):
        while True:
            x = self.read()
            self.boardread1(x)
            self.boardread2(x)

            p2 = int (input ('다른 파일을 보기를 원하시면 1번 나가기 2번'))
            if p2 == 2:
                break


    def boardfind(self):
        x = self.read()


        self.find(x)






    def modify(self):
        x = self.read()


        w , y= self.modify1(x)
        if w == 10:
            y1 = int(input('1.제목수정 2.내용수정 '))
            x = self.modify2(x, y, y1)

            self.save(x)






