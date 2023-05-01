# 문자열 출력
sentece = '나는 소년입니다.'
print(sentece)
sentece2 = "파이썬은 쉬워요."
print(sentece2)
sentece3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentece3)

# 슬라이싱
idNum = "980711-1234567"
print("성별: " + idNum[7])
print("년: " + idNum[:2])
print("월: " + idNum[2:4])
print("일: " + idNum[4:6])

print("생년월일: " + idNum[:6])
print("주민번호 뒷자리: " + idNum[7:])

# 뒤에서부터 가져올 수도 있음
print("주민번호 뒷자리: " + idNum[-7:])