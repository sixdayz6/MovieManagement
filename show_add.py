MovieList = []
CommentList = []
RateList = []

def add_movie():
    title = input("영화 제목을 입력하세요: ")
    tema = input("영화 테마를 입력하세요: ")
    running_time = input("상영시간을 입력하세요 (분 단위): ")
    start_date = input("개봉일자를 입력하세요 (YYYY-MM-DD): ")
    movie = {"title": title, "tema": tema, "running_time": running_time, "start_date":start_date}

    MovieList.append(movie)

    print(f"[입력완료] {title} 입력하신 영화가 추가되었습니다.")

def show_movies():
    if not MovieList:
        print("현재 등록된 영화가 없습니다.")
        return
    print("=== 등록된 영화 목록 ===")
    for idx, movie in enumerate(MovieList, 1):
        print(f"{idx}. 제목: {movie['title']} | 테마: {movie['tema']} | 상영시간: {movie['running_time']}분 | 개봉일: {movie['start_date']}")
    print()
