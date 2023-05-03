import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with를 사용한 파일쓰기
# 매번 close()를 해줄 필요 없음
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with를 사용한 파일읽기
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())