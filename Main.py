import show_add as sa

MovieList = []
CommentList = []
RateList = []

while True:
    choice = input('''
                다음 기능 중에서 선택해주세요.
                C.조회
                I.입력
                D.삭제
                U.수정
                R.영화평점 매기기
                M.영화 댓글 남기기
                V.댓글 조회
                Q.종료
                   ''').upper()
    
    if choice == "C":
        sa.show_movies()
    elif choice == "I":
        sa.add_movie()
    elif choice == "D":
        pass
    elif choice == "U":
        pass
    elif choice == "R":
        pass
    elif choice == "M":
        pass
    elif choice == "V":
        pass
    elif choice == "Q":
        break
    else:
        print("기능들 중에서 선택해 주세요.")
    
