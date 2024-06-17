# 데이터 프레임 : 엑셀의 표 형태로 구성된 데이터 분석의 가장 기본적인 자료 구조

import pandas as pd

# 샘플 데이터 프레임 생성 (딕셔너리)
data = pd.DataFrame({
    'name' : ['hong', 'kang', 'kim', 'park'] ,
    'age' : [24, 32, 43, 17] ,
    'addr' : ['서울', '경기', '제주', '부산']
})

print(data) # 알아서 이름, 나이, 주소를 표형태로 만들어준다.

# 엑셀로 저장하기
data.to_excel("day05/data/excel03.xlsx", index=False)

print("ㅡ" * 30)

# 2차원 리스트를 데이터 프레임에 넣기
source = [
    [1, '남자', 98, 88, 64] ,
    [2, '여자', 88, 90, 62, 72] ,
    [1, '남자', 92, 70, None, None] ,
    [3, '여자', 63, 60, 31, 70] ,
    [4, '남자', 120, 50, None, 88] 
]

data2 = pd.DataFrame(source)
data2.to_excel("day05/data/excel04_1.xlsx", index=False)

# 컬럼명과 인덱스를 만들어서 넣어주자
data3 = pd.DataFrame(source , 
                     columns=['학년', '성별', '국어', '영어', '수학', '과학'] , 
                     index=['철수', '영희', '민수', '수연', '호영'])
data3.to_excel("day05/data/excel04_2.xlsx")




