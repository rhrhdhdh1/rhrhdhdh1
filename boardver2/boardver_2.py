from boardver2 import login_ver2, boardclass

Id , ww = login_ver2.login('loginfile.txt')
b = boardclass.boardclass1('boardfile.txt')

while True:
    print('----------------------------')
    print('----------게시판-------------')
    print('----------------------------')
    print('------1. 게시글 작성----------')
    print('------2. 게시글 확인----------')
    print('------3. 게시글 검색----------')
    print('------4. 수정 및 삭제---------')
    print('----------------------------')


    sel = int(input('원하는 번호를 입력하세요.'))

    if sel == 1:
        b.boardwrite(Id)

    if sel == 2:
        while True:
            b.boardread()
            p2 = int(input('다른 파일을 보기를 원하시면 1번 나가기 2번'))
            if p2 == 2:
                break
    if sel == 3:
        b.boardfind()

    if sel == 4:
        b.modify()