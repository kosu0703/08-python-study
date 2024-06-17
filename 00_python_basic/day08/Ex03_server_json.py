# 서버로 가서 읽어오려면 urllib 가 필요하고
# json 데이터를 읽기 위해서 json 이 필요
from urllib.request import urlopen
import json

myurl = "http://localhost:8090/test07.do"
response = urlopen(myurl)
#print(response)

data = json.load(response)
#print(data)

# json 은 파싱이 따로 없고, 딕셔너리와 같다.

# 리스트 안에 딕셔너리가 있다.
for i in data :
    print(i['시·도별(1)'], end="  ")    
    print(i['총인구 (명)'], end="  ")    
    print(i['1차 접종 누계'], end="  ")    
    print(i['2차 접종 누계'], end="  ")    
    #print(i['1차 접종 퍼센트'], end="  ")    
    #print(i['2차 접종 퍼센트'])    
    print('{:.1f}%' .format(i['1차 접종 퍼센트']), end="  ")
    print('{:.1f}%' .format(i['2차 접종 퍼센트']))
    
    





