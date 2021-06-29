x=[]

def ADD(): # 회원가입

    a = None
    b = None
    c = None

    a = input('이름:')
    b = input('번호:')
    c = input('생일:')

    c1 = int(input('1번 등록 2번 취소\n'))

    if c1 == 0:
        print('취소되었습니다.')
    #    continue
    elif c1 == 1:

        y = dict(zip(['name','phone', 'brith'], [a, b, c]))

        x.append(y)

        z = len(x)
        print(y,'가', z,'번으로저장되었습니다.')

    return x


def Print1(c): #특정 인덱스 프린트
    a = list(x[c].keys())
    b = list(x[c].values())
    for q , w in zip(a , b):
        print('{} -- {}'.format(q , w))


def Print(): #전체 프린트
    for index, value in enumerate(x):
        print(index,'번',value)


def Find():
    q = int(input('0이름, 1번호, 2생일\n'))
    q1 = list(x[0].keys())
    q2 = q1[q]
    print(q2)
    a = input('검색 정보를 입력하세요.\n')
    for z in range(len(x)):
        if a == x[z][q2]:
            print(z,'번',x[z])

def Modify():
    m = int(input('수정하실 번호를 입력하세요.\n'))
    m1 = int(input('수정할 내용을 선택하세요. \n 0이름, 1번호, 2생일, 3취소\n'))
    if m1 == 3:
        print('취소하였습니다.')
    else:
        q1 = list(x[0].keys())
        q2 = q1[m1]
        m3 = input( '변경할 내용을 입력하세요\n')
        x[m][q2] = m3

        return x

while True:

    print('--------------------------')

    w = int(input('1입력 2인쇄 3검색 4수정 0취소\n'))


    if w == 1:
        ADD()


    if w == 2:
        a2 = int(input('1전체인쇄 2입력한 번호 인쇄'))
        if a2 == 1:
            Print()
        elif a2 == 2:
            a3 = int(input('번호를 입력하세요.'))
            Print1(a3)
        else:
            continue



    if w == 3:
        Find()

    if w == 4:
        Modify()

    else :
        continue

