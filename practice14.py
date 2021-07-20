# 7-3. 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("이영자", 20, "파이썬")
profile("송은이", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("이영자")
profile("송은이")




# 7-4. 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="이영자", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="송은이")