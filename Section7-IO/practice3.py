# write: 파일쓰기
# score_file = open("score.txt", "w", encoding="utf=8")
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# append: 이어쓰기
# score_file = open("score.txt", "a", encoding="utf=8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# read: 파일읽기
# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf=8")
# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# while문을 사용해서 읽기
# score_file = open("score.txt", "r", encoding="utf=8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='') # end를 사용해 줄바꿈 안 하기
# score_file.close()

# list를 사용해서 읽기
score_file = open("score.txt", "r", encoding="utf=8")
lines = score_file.readlines()
for line in lines:
    print(line)
score_file.close()