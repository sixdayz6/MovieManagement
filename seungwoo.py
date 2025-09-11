
MovieList = []
CommentList = []
RateList = [{'title':'귀멸의 칼날', 'rate':10}]

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
    
