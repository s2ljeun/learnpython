# 8-1. 표준입출력

# sep="", end=""
print("Python", "Java", "JavaScript", sep=",", end="?") #문장 끝을 줄바꿈이 아닌 물음표로 바꾼다
print("무엇이 더 재밌을까요?")



# file=sys.stdout, file=sys.stderr
import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준에러



# ljust(), rjust() - 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key와 value쌍으로 튜플
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # n칸의 자리 확보 후 좌/우 정렬



# zfill() - 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3칸의 자리 확보 후 빈 공간 0으로 채운다



# input을 통해 사용자에게 받은 값은 늘 문자열
answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) = str
print("입력하신 값은 " + answer + "입니다.")
