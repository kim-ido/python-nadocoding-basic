# 숫자 처리 함수
print(abs(5)) # 절대값: 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 10)) # 최대값: 10
print(min(5, 10)) # 최소값: 5
print(round(3.14)) # 반올림: 3

from math import * # math 라이브러리 전체 불러오기
print(floor(4.99)) # 내림: 4
print(ceil(3.14)) # 올림: 4
print(sqrt(16)) # 제곱근: 4

# 랜덤 함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 난수 생성
print(random() * 10) # 0.0 ~ 10.0 미만의  난수 생성
print(int(random() * 10)) # 0 ~ 10 미만의 난수 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 난수 생성

# 로또 번호 생성기
# 방법 1
print(int(random() * 45) + 1) # 1 ~ 45 이하의 난수 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 난수 생성
# 방법 2
print(randrange(1, 46)) # 1 ~ 46 미만의 난수 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 난수 생성
# 방벙 3
print(randint(1, 45)) # 1 ~ 45 이하의 난수 생성
print(randint(1, 45)) # 1 ~ 45 이하의 난수 생성


