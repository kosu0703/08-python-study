# json 데이터를 쉽게 처리하고자 사용하는 모듈

import json

with open('day07/myinfo.json', 'r', encoding='utf-8') as f :
    data = json.load(f)
    
print(data, type(data)) # 딕셔너리

print("ㅡ" * 30)

d = {"name" : "둘리", "birth" : "0101", "age" : 24}

j_data = json.dumps(d)
# 한글이 깨진 것처럼 보이지만 다시 json.loads 를 하면 제대로 나온다.
print(j_data)
print(json.loads(j_data))

# 아니면 dumps 에 아스키코드 옵션을 주면 깨지지 않는다.
j_data2 = json.dumps(d, ensure_ascii=False)
print(j_data2)

print("ㅡ" * 30)





