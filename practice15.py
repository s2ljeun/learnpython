# 7-5. 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("이영자", 20, "Python", "Java", "C", "C++", "C#")
# profile("송은이", 25, "Kotlin", "Swift", "", "", "")


def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")       
    print()


profile("이영자", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("송은이", 25, "Kotlin", "Swift")