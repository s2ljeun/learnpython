# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

#     * 표준 체중 : 각 개인의 키에 적당한 체중

#     (성별에 따른 공식)
#     남자: 키(m) x 키(m) x 22
#     여자: 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.



# 내 풀이
weight = 0 # 전역변수 weight 지정

def std_weight(weight, height, gender):
    if gender == "여자":
        weight = height * height * 21
        return weight
    else:
        weight = height * height * 22
        return weight

weight = std_weight(weight, 1.75, "여자")
print("키 175cm 여자의 표준 체중은 {0:.2f}kg 입니다.".format(weight))

weight = std_weight(weight, 1.75, "남자")
print("키 175cm 남자의 표준 체중은 {0:.2f}kg 입니다.".format(weight))



# 강사 풀이
def std_weight(height, gender):
    if gender == "여자":
        return height * height * 21
    else:
        return height * height * 22

height = 175
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))




# # 소수점 원하는 자리수에서 반올림 후 출력하기 // 반올림 안 하는 방법??
# # 1
# ans = 10.5361
# print('%.2f' %ans)

# # 2
# ans = 10.5361
# print("{0:.2f}".format(ans))
# print("{0:.2f}하고 {1:.3f}".format(ans, ans))