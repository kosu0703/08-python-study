from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

params ={'serviceKey' : 'Rs2hCA9I6Y5q4TlZWwvkT+Kpf/E42e4y5TcRt9HlhfxZzg6r/Zb7PyaQBN/v183KSU91M9jKg8OvM6pN2TAMAw==', 
         'returnType' : 'xml', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'sidoName' : '서울', 
         'ver' : '1.0' }

query_string = urlencode(params)

# 파이썬의 f-string을 사용하여 문자열을 조립하는 방식
# f"{url}?{query_string}"은 url과 query_string을 합쳐서 하나의 완전한 URL을 형성
myurl = f"{url}?{query_string}"

response = urlopen(myurl)

soup = BeautifulSoup(response, "html.parser")
#print(soup)

c_item = soup.find_all('item')

for i in c_item :
    # 태그 글자 추출 => get_text() 또는 string
    print(i.select_one('stationName').string , end="  ")
    print(i.select_one('pm10Value').string , end="  ")
    print(i.select_one('pm25Value').string)
    
    # find 는 소문자로 해야 나옴
    print(i.find('stationname').get_text() , end="  ")
    print(i.find('pm10value').get_text() , end="  ")
    print(i.find('pm25value').get_text())


    


