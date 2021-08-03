# 8-3. 파일입출력
 # 파일 생성
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file) # 내용 쓰기
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기(필수)


# 이어쓰기(append)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


# 파일 읽기
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()


# 파일 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


# 몇 줄인지 모르는 파일 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    else:
        print(line)
score_file.close()


# 몇 줄인지 모르는 파일 리스트로 변형해서 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")