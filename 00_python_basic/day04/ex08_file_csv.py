# 딕셔너리 입/출력

import csv

# 쓰기
with open("day04/data/csv03.csv" , 'w' , encoding='utf-8' , newline='') as f1 :
    # 키값
    fname = ['name', 'age', 'addr'] 
    
    wr = csv.DictWriter(f1, fieldnames=fname)
    
    # 키값 => 컬럼명
    wr.writeheader()
    
    wr.writerow({
        'name' : 'hong' ,
        'age' : 24 ,
        'addr' : '서울' 
    })
    wr.writerow({
        'name' : 'kang' ,
        'age' : 14 ,
        'addr' : '인천' 
    })
    wr.writerow({
        'name' : 'ko' ,
        'age' : 32 ,
        'addr' : '제주' 
    })

# CSV 파일에는 value 값만 표시된다.

# 읽기
with open("day04/data/csv03.csv" , 'r' , encoding='utf-8') as f2 :
    rd = csv.DictReader(f2)
    
    for i in rd :
        print(i['name'], i['age'], i['addr'])
        




# 성인 , 미성년자 추가하기
with open("day04/data/csv03.csv" , 'r' , encoding='utf-8' ) as f3 :
    rd = csv.DictReader(f3)
    lines = []  
    for i in rd :
        if int(i['age']) <= 18 :
            i['adult'] = '미성년자'
        else :
            i['adult'] = '성인'
        lines.append(i)

with open("day04/data/csv04.csv", 'w' , encoding='utf-8' , newline='') as f4 :
    f_name = ['name', 'age' , 'addr' ,'adult']
    wr = csv.DictWriter(f4, fieldnames=f_name)
    wr.writeheader()
    wr.writerows(lines)



