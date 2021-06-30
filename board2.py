import login3
import board2_1

ID , ww =login3.Login1()

while True:
    sel = int(input('1.게시글 작성 2.게시글 확인 3.게시글 검색 4.수정 및 삭제'))

    if sel == 1:
        board2_1.UPload()

    if sel == 2:
        board2_1.Read0()

    if sel == 3:
        board2_1.Search()

    if sel == 4:
        board2_1.Modify1()


#
# if __name__=="__main__":
#     main()