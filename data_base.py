import sqlite3

# 파일 경로는 실제 파일이 있는 위치로 바꿔야 합니다.
connect = sqlite3.connect('D:/DataBase/to_do_list_2025.db')

# 커서 객체 생성
cursor = connect.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)


res = cursor.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
# 이걸로 내가 지금 어떤 DB랑 연관이 되어있는지 확인 하는 것이다.


cursor.execute("""
    INSERT INTO to_do_list VALUES
        ('할머니 생신 밥먹기', '2025-01-20', 2,1),
        ('테니스 치기 4번 코트 2시', '2025-01-23', 3,0)
""")
# 넣을 데이터 쓰기

connect.commit()
# 데이터 넣기


