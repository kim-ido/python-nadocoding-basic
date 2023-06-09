# def profile(name, age, main_lang):
#     print(f'이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}')

# profile('유재석', 20, '파이썬')
# profile('김태호', 25, '자바')

# 같은 학교 같은 학년 같은 반 같은 수업

# 기본값
def profile_default(name, age=17, main_lang='파이썬'):
    print(f'이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}')

profile_default('유재석')
profile_default('김태호')

# 키워드값
def profile_keyword(name, age, main_lang):
    print(name, age, main_lang)

profile_keyword(name='유재석', main_lang='파이썬', age=20)
profile_keyword(main_lang='자바', age=20, name='김태호')