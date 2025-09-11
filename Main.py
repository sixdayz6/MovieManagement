MovieList = []
CommentList = []
RateList = []
import sys
import re

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
            self.show_movies()
        elif choice == "I":
            self.add_movie()
        elif choice == "D":
            self.deleteMovie()
        elif choice == "U":
            self.updateMovie()
        elif choice == "R":
            self.rateMovie()
        elif choice == "M":
            self.comment()
        elif choice == "V":
            self.viewComment()
        elif choice == "Q":
            print("프로그램 종료")
            sys.exit()
        else:
            print("메뉴 선택을 잘못하셨습니다. 다시 선택해 주세요.")
    # 1. 영화 추가
    def add_movie(self):
        title = input("영화 제목을 입력하세요: ")
        tema = input("영화 테마를 입력하세요: ")
        running_time = input("상영시간을 입력하세요 (분 단위): ")
        while True:
            start_date = input("개봉일자를 입력하세요 (YYYY-MM-DD): ")
            pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    
            if re.fullmatch(pattern, start_date):
                print(f"입력 완료: {start_date}")
                break
            else:
                print("잘못된 형식입니다. YYYY-MM-DD 형식으로 입력해주세요 (월 01~12, 일 01~31).")
        
        rate = input("평점을 매겨주세요")
        movie = {"title": title, "tema": tema, "running_time": running_time, "start_date":start_date, "rate":rate}
        print(f"[입력완료] {title} 입력하신 영화가 추가되었습니다.")  
        self.MovieList.append(movie)    
            
            


    # 2. 영화 조회
    def show_movies(self):
        if not self.MovieList:
            print("현재 등록된 영화가 없습니다.")
            return
        print("=== 등록된 영화 목록 ===")
        for idx, movie in enumerate(self.MovieList, 1):
            print(f"{idx}. 제목: {movie['title']} | 테마: {movie['tema']} | 상영시간: {movie['running_time']}분 | 개봉일: {movie['start_date']} | 평점:{movie['rate']}")
        print()


     #3. 영화 업데이트
    def updateMovie(self):
        print('영화 정보 수정입니다')
        while True:
            choice = input("수정하시려는 영화 이름을 입력하세요 (종료하려면 exit 입력): ")
            if choice == 'exit':
                break

            idx = -1
            for i in range(len(self.MovieList)):
                if self.MovieList[i]['title'] == choice:
                    idx = i
                    break
            
            if idx == -1:
                print("등록되지 않은 영화 이름입니다.")
                continue

            choice1 = input('''다음 중 수정하실 정보 골라주세요
                title, tema, duration, rating, startDate
                (수정할 정보가 없으면 'exit' 입력): ''')

            if choice1 in ('title', 'tema', 'duration', 'rating', 'startDate'):
                self.MovieList[idx][choice1] = input('수정할 {} 을 입력하세요: '.format(choice1))
                print("수정 완료!")
            elif choice1 == 'exit':
                continue
            else:
                print("존재하지 않는 정보입니다.")

    #4. 영화 삭제
    def deleteMovie(self):
        print("삭제입니다 ")
        while True:
            title = input('삭제하려는 영화의 영화 이름을 입력하세요 >>> ').strip()
            for idx,i in enumerate(self.MovieList):
                if i['title'] == title:
                    data = self.MovieList.pop(idx)
                    print('{}영화의 정보가 삭제되었습니다.'.format(data['name']))
                    break
                else:
                    print('등록되지 않은 영화 이름입니다.')
                    print(self.MovieList)
        

    # 5. 영화평점 매기기
    def rateMovie(self, RateList):
        title = input('평가하고 싶은 영화 제목 입력 >>>')
        for i in range(0, len(self.MovieList)):
            while self.MovieList[i]['title'] == title:
                rate = int(input("0에서 10 사이의 정수로 영화를 평가해주세요."))
                RateList.append({'title':title, 'rate':rate})
                print(f"\"{title}\"에{rate}점이 평가 됐습니다.")
                break
            else:
                print('영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.')

# 6. 영화 댓글 남기기
    def comment(self, CommentList):
        title = input('댓글 남기고 싶은 영화 제목 입력 >>>')
        for i in range(0, len(self.MovieList)):
            while self.MovieList[i]['title'] == title:
                comment = input('영화에 남기고 싶은 말을 입력해주세요 >>>')
                CommentList.append({'title':title, 'comment':comment})
                print(f"\"{title}\"에 댓글 \'{comment}\'이 남겼습니다.")
                break
            else:
                print('영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.')

# 7. 댓글 조회
    def viewComment(self, CommentList):
        title = input('댓글 남기고 싶은 영화 제목 입력 >>>')
        viewCommentList = []
        for i in range(0, len(CommentList)):
            if CommentList[i]['title'] == title:
                viewCommentList.append(CommentList[i]['comment'])
            
        print(f"\"{title}\"에 대한 댓글 입니다. \nviewCommentList")

    # 일단은 영화 조회 기능을 사용할 때마다 RateList에서 평점을 꺼내와서 모두 더한 후에 MovieList의 Rate에 입력해준다.
    def updateRate(self, RateList):
        totalRate = 0
        div = 0
        title = input('댓글 남기고 싶은 영화 제목 입력 >>>')
        for i in range(0, len(RateList)):
            if RateList[i]['title'] == title:
                totalRate += RateList[i]['rate']
                div += 1
            else:
                print("영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.")
        
        resultRate = round(totalRate/div, 1)
        print(resultRate)
        for i in range(0, len(MovieList)):
            while self.MovieList[i]['title'] == title:
                self.MovieList[i]['rate'] = resultRate
                break

            else:
                print("영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.")

if __name__ == "__main__":
    MovieManagement()
       
        
    
    
    
