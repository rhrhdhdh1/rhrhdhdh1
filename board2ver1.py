import login3ver1
import board2_1ver1

ID , ww =login3ver1.Login1()

print(globals())
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
        board2_1ver1.UPload(ID)

    if sel == 2:
        while True:
            board2_1ver1.Read0()
            p2 = int(input('다른 파일을 보기를 원하시면 1번 나가기 2번'))
            if p2 == 2:
                break
    if sel == 3:
        board2_1ver1.Search()

    if sel == 4:
        board2_1ver1.Modify1()


#
# if __name__=="__main__":
#     main()