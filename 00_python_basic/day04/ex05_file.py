# with 문과 함께 사용하기
# 파일을 열면 항상 close 해줘야 한다.
# 이를 자동으로 처리해주는 역할을 with 문이 한다.

# with open('경로' , '모드(r, w, a)', encoding="utf-8") as 이름 :

with open("day04/data/text04.txt" , 'w' , encoding='utf-8') as f1 :
    f1.write("한국 ICT 인재 개발원\n")
    f1.write("5강의실")
    
with open("day04/data/text04.txt" , 'r' , encoding='utf-8') as f2 :
    data = f2.read()
    
print(data)
    

    
    
    
    
    
