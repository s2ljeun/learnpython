# 8-4. pickle

import pickle # 피클 모듈 불러오기
profile_file = open("profile.pickle", "wb") # 바이너리 타입, 인코딩 설정 X
profile = {"이름": "장도연", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 바이너리 타입, 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()