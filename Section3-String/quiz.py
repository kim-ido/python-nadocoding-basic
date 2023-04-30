'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙 1: http:// 부분은 제외 => naver.com
규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3: 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!"로 구성 => (nav)(5)(1)(!)

예) 생성된 비밀번호: nav51!
'''

url = "http://google.com"
# 규칙 1
url1 = url[7:]
# 규칙 2
url2 = url1[:-4]
# 규칙 3
pw = url2[:3] + str(len(url2)) + str(url2.count("e")) + "!"
# 출력
print(f"생성된 비밀번호: {pw}")