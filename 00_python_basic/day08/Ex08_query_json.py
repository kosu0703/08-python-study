from urllib.request import urlopen
from urllib.parse import urlencode
import json

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

params ={'serviceKey' : 'Rs2hCA9I6Y5q4TlZWwvkT+Kpf/E42e4y5TcRt9HlhfxZzg6r/Zb7PyaQBN/v183KSU91M9jKg8OvM6pN2TAMAw==', 
         'returnType' : 'json', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'sidoName' : '서울', 
         'ver' : '1.0' }

query_string = urlencode(params)

# 파이썬의 f-string을 사용하여 문자열을 조립하는 방식
# f"{url}?{query_string}"은 url과 query_string을 합쳐서 하나의 완전한 URL을 형성
myurl = f"{url}?{query_string}"

response = urlopen(myurl)
data = json.load(response)
#print(data)

c_item = data['response']['body']['items']
for i in c_item :
    print(i['stationName'] , end='  ')
    print(i['pm10Value'] , end='  ')
    print(i['pm25Value'])













