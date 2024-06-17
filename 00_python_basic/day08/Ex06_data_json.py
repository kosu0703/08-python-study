import requests
import json

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

params ={'serviceKey' : 'Rs2hCA9I6Y5q4TlZWwvkT+Kpf/E42e4y5TcRt9HlhfxZzg6r/Zb7PyaQBN/v183KSU91M9jKg8OvM6pN2TAMAw==', 
         'returnType' : 'json', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'sidoName' : '서울', 
         'ver' : '1.0' }

response = requests.get(url, params=params)
#print(response.content)

# json.load() : 파일 객체에서 json 데이터를 읽어서 파이썬 객체로 변환 (주로 파일을 열때)
# json.loads() : json 형식의 문자열을 파이썬 객체로 변환(주로 네트워크를 통해 수신된 json)
data = json.loads(response.content)
#print(data)

# json 은 파싱이 따로 없고, 딕셔너리와 같다.
c_item = data['response']['body']['items']
#c_item = data.get('response').get('body').get('items')
#print(c_item)

# 리스트 안에 딕셔너리가 있다.
for i in c_item :
    print(i['stationName'] , end='  ')
    print(i['pm10Value'] , end='  ')
    print(i['pm25Value'])








