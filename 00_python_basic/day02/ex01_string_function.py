# 문자열 관련 함수들 : 문자열 뒤에 .(점) 을 붙인 후 함수 이름을 써주면 된다.

# 문자 갯수 => count
str = "hobby"
print("문자 갯수 : " , str.count('b'))
print("ㅡ" * 30)

# 문자 위치 알려주기 => find, index
print("find")
print(str.find('b'))
print(str.find('k')) # find 는 문자가 없으면 -1
print("ㅡ" * 30)

print("index")
print(str.index('b'))
#print(str.index('k')) # index 는 문자가 없으면 오류 발생
print("ㅡ" * 30)

# 문자열 삽입 => join
print("join")
print("," .join(str)) 
print("ㅡ" * 30)
# str 이 가지고 있는 문자열에서 각각의 문자 사이에 , 콤마가 삽입된다.
# ** 리스트나 튜플에도 사용가능하다.
# ** 문자열이나 튜플은 불변형 자료형이라 join 을 사용하면 새롭게 만들어진다.

# 소문자를 대문자로 변환 => upper
print(str.upper())
# 대문자를 소문자로 변환 => lower
print(str.upper().lower())
# 첫글자만 대문자, 나머지 소문자 => capitalize
print(str.capitalize())
print("ㅡ" * 30)

str = "   hello   "
print(len(str))
# 왼쪽 공백 지우기 => lstrip
print(str.lstrip() , len(str.lstrip()))
# 오른쪽 공백 지우기 => rstrip
print(str.rstrip() , len(str.rstrip()))
# 양쪽 공백 지우기 => strip
print(str.strip() , len(str.strip()))
print("ㅡ" * 30)

# 문자열 바꾸기 => replace(찾는 문자열, 바꿀 문자열)
str = "Life is too short"
print(str.replace("Life" , "Your leg"))
print("ㅡ" * 30)

# 문자열 나누기 => split(구분자)  
print(str.split()) # 구분자를 생략하면 스페이스, 탭, 엔터를 기준으로 구분한다.
print("ㅡ" * 30)



