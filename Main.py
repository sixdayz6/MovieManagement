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
        

    # 4. 영화평점 매기기
    def rateMovie(MovieList, RateList):
        title = input('평가하고 싶은 영화 제목 입력 >>>')
        for i in range(0, len(MovieList)):
            while MovieList[i]['title'] == title:
                rate = int(input("0에서 10 사이의 정수로 영화를 평가해주세요."))
                RateList.append({'title':title, 'rate':rate})
                print(f"\"{title}\"에{rate}점이 평가 됐습니다.")
                break
            else:
                print('영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.')

# 5. 영화 댓글 남기기
    def comment(MovieList, CommentList):
        title = input('댓글 남기고 싶은 영화 제목 입력 >>>')
        for i in range(0, len(MovieList)):
            while MovieList[i]['title'] == title:
                comment = input('영화에 남기고 싶은 말을 입력해주세요 >>>')
                CommentList.append({'title':title, 'comment':comment})
                print(f"\"{title}\"에 댓글 \'{comment}\'이 남겼습니다.")
                break
            else:
                print('영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.')

    # 6. 댓글 조회
    def veiwComment(CommentList):
        title = input('댓글 남기고 싶은 영화 제목 입력 >>>')
        veiwCommentList = []
        for i in range(0, len(CommentList)):
            if CommentList[i]['title'] == title:
                veiwCommentList.append(CommentList[i]['comment'])
            
        print(f"\"{title}\"에 대한 댓글 입니다. \nveiwCommentList")

    # 일단은 영화 조회 기능을 사용할 때마다 RateList에서 평점을 꺼내와서 모두 더한 후에 MovieList의 Rate에 입력해준다.
    def updateRate(MovieList, RateList, title):
        totalRate = 0
        div = 0
        for i in range(0, len(RateList)):
            if RateList[i]['title'] == title:
                totalRate += RateList[i]['rate']
                div += 1
            else:
                print("영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.")
        
        resultRate = round(totalRate/div, 1)
        print(resultRate)
        for i in range(0, len(MovieList)):
            while MovieList[i]['title'] == title:
                MovieList[i]['rate'] = resultRate
                break

            else:
                print("영화 제목을 잘 못 입력하셨습니다. 다시 입력해 주세요.")
        
       
        
    
    
    
