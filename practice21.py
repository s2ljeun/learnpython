# 8-5. with

import pickle


# pickle과 with

with open("profile.pickle", "rb") as profile_file: # profile_file 변수에 저장
    print(pickle.load(profile_file)) # close할 필요 없음


# with로 파일 쓰기
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

# with로 파일 불러오기
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())