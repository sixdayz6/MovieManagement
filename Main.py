import show_add as sa

MovieList = []
CommentList = []
RateList = []
import sys

class MovieManagement():

    def __init__(self):
        self.MovieList = []
        self.CommentList = []
        self.RateList = []
        while True:
            self.exe(self.display())

    def display(self):
        choice = input('''
        다음 기능 중에서 선택해주세요.
        C - 조회
        I - 입력
        D - 삭제
        U - 수정
        R - 영화평점 매기기
        M - 영화 댓글 남기기
        V - 댓글 조회
        Q - 종료
        ''').upper()
        return choice
    
    def exe(self, choice):
        if choice == "C":
            pass
        elif choice == "I":
            pass
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
            print("프로그램 종료")
            sys.exit()
        else:
            print("메뉴 선택을 잘못하셨습니다. 다시 선택해 주세요.")

    
    
    
<<<<<<< HEAD
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
=======
>>>>>>> 57b2c5291a4fc886a156ae66eac041aecb9d0c79
    
