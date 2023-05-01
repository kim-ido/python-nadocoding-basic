# 딕셔너리

cabinet = {3:"유재석", 100:"박명수"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 에러 O
print(cabinet.get(5)) # 에러 X
print(cabinet.get(5, "사용 가능"))

# key in 변수
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"박명수"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# 둘 다 출력
print(cabinet.items())

# 목욕탕 폐업
cabinet.clear()
print(cabinet)