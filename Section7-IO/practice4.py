# 피클: 파일 안의 데이터 사용하기
import pickle
# 피클 사용을 위해서는 바이너리 타입 정의가 필요함
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프" , "코딩"]}
# print(profile)
# # profile에 있는 정보를 file에 저장
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()