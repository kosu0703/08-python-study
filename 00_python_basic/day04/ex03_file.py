'''
    파일 입/출력
    
    이름 = open( '파일이름' , 옵션 )
    --  중간 과정 --
    이름.close()
    
    
    ** 옵션
    - r 모드 : 읽기
    - w 모드 : 쓰기 (기존 파일이 있으면 덮어쓰기가 되고, 없으면 새로 생성한다.)
    - a 모드 : 추가

'''

f = open('day04/data/text03.txt', 'w', encoding='utf-8')

for i in range(1, 6) :
    str1 = '{}번째 줄 ... \n' .format(i)
    f.write(str1)

f.close()

# os 는 파이썬의 표준 라이브러리, 운영체제와 상호작용할 때 사용하며,
# 다양한 운영체제 관련 기능을 제공한다.
# 파일 및 디렉토리 관리, 파일 경로 관리 등
import os

# 현재 위치 저장하자
c_dir = os.path.dirname(__file__) # 내 파일이 있는 위치 => day04 폴더
#print(c_dir)
f_path = os.path.join(c_dir + "/data" , "text02.txt")

f = open(f_path, 'w', encoding='utf-8')

for i in range(1, 6) :
    str1 = '{}번째 줄 ... \n' .format(i)
    f.write(str1)
    
f.close()

# 파이썬에서 맨마지막은 포함되지 않는다.

print("ㅡ" * 30)

f = open('day04/data/text03.txt', 'r', encoding='utf-8')

while True :
    line = f.readline() 
    print(line)
    if not line : break
    
f.close()    

print("ㅡ" * 30)

f = open('day04/data/text03.txt', 'r', encoding='utf-8')

while True :
    lines = f.readlines() 
    #print(lines , type(lines)) # list 로 나온다
    for i in lines :
        print(i)
    if not lines : break
    
f.close()    

print("ㅡ" * 30)

f = open('day04/data/text03.txt', 'r', encoding='utf-8')
data = f.read()
print(data , type(data)) # str 로 나온다
f.close()



print("ㅡ" * 30)
