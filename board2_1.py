def UPload(): #파일 업로드
    import json

    with open('Broad.txt','r') as file:
        x1 = file.read()
    x = json.loads(x1)

    a = None
    b = None
    c = None
    d = None
    x1 = int(len(x))
    a = input('제목을 입력하세요.')
    b = input('내용을 입력하세요.')
    c = ID
    d = input('글 비밀번호를 입력하세요.')
    y = dict(zip(['Title','Contents', 'Id', 'Password'], [a, b, c, d]))
    x.append(y)

    x2 = json.dumps(x)
    with open('Broad.txt','w') as file1:
        file1.write(x2)

def Read1(x):
    for i in range(len(x)):
        a = i
        b = x[i]['Title']
        c = x[i]['Id']
        print('{}번 제목:{} 작성자 {}'.format(a,b,c))

def Read2(x):
    x3 = int(input('읽기를 원하시는 번호를 입력하세요'))
    a1 = x3
    b1 = x[x3]['Title']
    c1 = x[x3]['Id']
    d1 = x[x3]['Contents']

    print('{}번 제목 :{}           작성자:{}'.format(a1,b1,c1))
    print('내용')
    print(d1)


def Read0():
    import json
    with open('Broad.txt','r') as file:
        x1 = file.read()

    x = json.loads(x1)
    Read1(x)
    Read2(x)


def Search1(x , a):
    y = input('검색 내용을 입력하세요\n')
    for i in range(len(x)):
        if x[i][a] == y:
            a1 = i
            b1 = x[i]['Title']
            c1 = x[i]['Id']
            d1 = x[i]['Contents']
            print('{}번 제목 {}       작성자{}'.format(a1, b1, c1))
            print('내용')
            print(d1)

def Search2(x , a):
    y = input('검색 내용을 입력하세요\n')
    print(a,"=",y,'로 검색한 결과')
    for i in range(len(x)):
        if x[i][a].find(y) != -1:
            a1 = i
            b1 = x[i]['Title']
            c1 = x[i]['Id']
            d1 = x[i]['Contents']
            print('{}번 제목 {}       작성자{}'.format(a1, b1, c1))
            print('내용')
            print(d1)


def Search():
    import json

    with open('Broad.txt','r') as file:
        x1 = file.read()
    x = json.loads(x1)
    y = int(input('1.Id로 검색\n2.Contents로 검색\n3.Title로 검색\n'))
    if y == 1:
        a = 'Id'
        Search1(x, a)
    if y == 2 :
        a = 'Contents'
        Search2(x, a)
    if y == 3 :
        a = 'Title'
        Search2(x, a)


def Modify1():
    with open('Broad.txt','r') as file:
        x1 = file.read()
    x = json.loads(x1)
    y = int(input('수정을 원하는 글의 번호를 입력하세요.'))
    z = input('수정을 원하는 글의 비밀번호를 입력하세요.')

    if x[y]['Password'] == z:
        y1 = int(input('1.제목수정 2.내용수정 3.글 삭제'))
        if y1 == 1:
            z2 = x[y]['Title']
            z1 = input('수정할 내용을 입력하세요')
            x[y]['Title'] = z1
            print(z2,'에서',x[y]['Title'],'로 변경되었습니다.')

        if y1 == 2:
            z2 = x[y]['Contents']
            z1 = input('수정할 내용을 입력하세요')
            x[y]['Contents'] = z1
            print(z2,'에서',x[y]['Contents'], '로 변경되었습니다.')

        if y1 == 3:
            y2 = int(input('1.삭제 2.취소'))
            if y2 == 1:
                del x[y]
                print('삭제가 완료되었습니다.')
                Read1(x)
    x2 = json.dumps(x)
    with open('Broad.txt','w') as file1:
        file1.write(x2)