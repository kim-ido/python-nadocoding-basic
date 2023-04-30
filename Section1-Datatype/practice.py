# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+5)
print(2*5)
print(3*(2+1)+1)

# 문자열 자료형
print('토끼')
print("거북이")
print("아자아자 화이팅")
print("아자" * 2, "화이팅")

# boolean 자료형: 참 / 거짓
print(5 > 10) # false
print(5 < 10) # True
print(False) # false
print(True) # True
print(not True) # false
print(not False) # True
print(not (5 < 10)) # False
print(not (5 > 10)) # True

# 변수: 강아지 소개
animal = "강아지"
name = "고양이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리 집 " + animal + " 이름은 " + name + "에요.")
# 숫자 자료형, boolean 자료형을 print문에 사용하기 위해서는 형변환이 필요함
# ',' 사용시에는 형변환 필요없음
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요?", is_adult)

'''
이렇게 하면
여러 문장을 한 번에
주석 처리 가능함
'''