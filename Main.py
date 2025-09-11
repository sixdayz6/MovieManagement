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

    def updateMovie (movieList):
        print('영화 정보 수정입니다')
        while True:
            choice = input("수정하시려는 영화 이름을 입력하세요 (종료하려면 exit 입력): ")
            if choice == 'exit':
                break

            idx = -1
            for i in range(len(movieList)):
                if movieList[i]['title'] == choice:
                    idx = i
                    break
            
            if idx == -1:
                print("등록되지 않은 영화 이름입니다.")
                continue

            choice1 = input('''다음 중 수정하실 정보 골라주세요
                title, tema, duration, rating, startDate
                (수정할 정보가 없으면 'exit' 입력): ''')

            if choice1 in ('title', 'tema', 'duration', 'rating', 'startDate'):
                movieList[idx][choice1] = input('수정할 {} 을 입력하세요: '.format(choice1))
                print("수정 완료!")
            elif choice1 == 'exit':
                continue
            else:
                print("존재하지 않는 정보입니다.")


    def deleteMovie(movieList):
        print("삭제입니다 ")
        while True:
            title = input('삭제하려는 영화의 영화 이름을 입력하세요 >>> ').strip()
            for idx,i in enumerate(movieList):
                if i['title'] == title:
                    data = movieList.pop(idx)
                    print('{}영화의 정보가 삭제되었습니다.'.format(data['name']))
                    break
                else:
                    print('등록되지 않은 영화 이름입니다.')
                    print(movieList)
        

        
    
    
    
