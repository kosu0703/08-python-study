# 문자열 : 연속되 문자들의 나열 
#           "" 쌍따옴표 , '' 홑따옴표 , """ 내용 """ , ''' 내용 ''' 

str = '안녕 파이썬 !'
print(str , type(str))

str = "hello python !"
print(str , type(str))

# 두개를 같이 사용하는 경우
str = "I'm OK !!"
print(str , type(str))
str = 'I"m OK !!'
print(str , type(str))
# 이스케이프 문자 사용가능(역슬래시)
str = 'I\'m OK !!'
print(str , type(str))
str = 'I\"m OK !!'
print(str , type(str))

# 여러줄 사용할때
str = "안녕하세요\n반갑습니다"
print(str , type(str))

str = '''hi~~~
hello'''
print(str , type(str))

str = """안녕하세요
반갑습니다"""
print(str , type(str))

# 이스케이프 문자
# \n : 줄바꾸기
# \t : 탭(일정 간격 띄우기)
# \" : 쌍따옴표 " 표시
# \' : 홑따옴표 ' 표시



 


