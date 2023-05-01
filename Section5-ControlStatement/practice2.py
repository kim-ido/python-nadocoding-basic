# 반복문
# for
for waiting_num in range(1, 5):
    print('대기번호 : {}'.format(waiting_num))

starbucks = ['아이언맨', '토르', '그루트']
for customer in starbucks:
    print(f'{customer}, 커피가 준비되었습니다.')

# 한 줄로 끝내는 for
# 출석번호 앞에 100을 붙이기로 함
students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ['Iron man', 'Thor', 'I am groot']
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ['Iron man', 'Thor', 'I am groot']
students = [i.upper() for i in students]
print(students)

# while
customer = '토르'
print(customer)
index = 5

while index >= 1:
    print(f'{customer}, 커피가 준비되었습니다. {index} 번 남았어요.')
    index -= 1
    if index == 0:
        print('커피는 폐기처분되었습니다.')

# 토르가 올 때까지 반복
# customer = '토르'
# person = 'Unknown'
# while person != customer:
#     print(f'{customer}, 커피가 준비되었습니다.')
#     person = input("이름이 어떻게 되세요? ")