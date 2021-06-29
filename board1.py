import json

import login3

ID , ww =login3.Login1()

def UPload(): #파일 업로드
    import json

    with open('Broad.txt','r') as file:
        x1 = file.read()
    x = json.loads(x1)

    a = None
    b = None
    c = None

    x1 = int(len(x))
    a = input('제목을 입력하세요.')
    b = input('내용을 입력하세요.')
    c = ID

    y = dict(zip(['Title','Contents', 'Id'], [a, b, c]))
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

    print('{}번 제목 {}       작성자{}'.format(a1,b1,c1))
    print('내용')
    print(d1)


def Read0():
    import json
    with open('Broad.txt','r') as file:
        x1 = file.read()

    x = json.loads(x1)
    Read1(x)
    Read2(x)


while True:
    sel = int(input('1.게시글 작성 2.게시글 확인'))

    if sel == 1:
        UPload()

    if sel == 2:
        Read0()



