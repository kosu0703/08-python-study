import random, os, shutil

# random : 난수 발생 
print(random.random()) # 0.0 ~ 1.0 미만
print(int(random.random() * 5)) # 0 ~ 4
print(random.randint(1, 10)) # 1 ~ 10 (끝포함 됨!)

print("ㅡ" * 30)

# 리스트 항목을 무작위로 섞는다.
data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data)))

print("ㅡ" * 30)

# os : 환경변수나 디렉토리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
'''
    os.environ : 시스템 환경 변수 값들을 보여주는 역할을 한다.
                    시스템 정보를 딕셔너리 객체로 반환
                
    os.chdir : 현재 디렉토리의 위치를 변경하는 함수
    
    os.getcwd : 자신의 현재 디렉토리의 위치를 반환
    
    os.system("명령어") : 시스템의 유틸리티나 dos 명령어들을 파이썬에서 호출
    
    os.popen : 시스템 명렁어를 시킨 결과값을 읽기 모드의 파일 객체로 반환
    
    os.path.dirname(__file__) : 현재 위치 저장
    
    os.mkdir(디렉토리명) : 디렉토리 생성
    os.rmdir(디렉토리명) : 디렉토리 삭제 (비이있을 때만)
    
    os.rename(원본_파일_이름, 변경할_파일_이름)
    
''' 
print(os.environ) # 시스템 정보 => 딕셔너리 (key : value)

print("ㅡ" * 30)

# 현재 폴더까지(파일의 현재 위치)
print(os.path.dirname(__file__)) 

# 상위 폴더까지(터미널과 같음)
print(os.getcwd()) 




print("ㅡ" * 30)

# shutil : 파일 복사해주는 모듈



