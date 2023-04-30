# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

# 인덱스
index = python.index("n")
print(index)
# 첫번째 n 다음부터 찾기
index = python.index("n", index + 1)
print(index)

# 실행오류 O
#print(python.index("Java"))
# 실행오류 X
print(python.find("Java"))

# count
print(python.count("n"))