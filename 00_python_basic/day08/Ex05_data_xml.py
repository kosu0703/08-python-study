from bs4 import BeautifulSoup
import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

params ={'serviceKey' : 'Rs2hCA9I6Y5q4TlZWwvkT+Kpf/E42e4y5TcRt9HlhfxZzg6r/Zb7PyaQBN/v183KSU91M9jKg8OvM6pN2TAMAw==', 
         'returnType' : 'xml', 
         'numOfRows' : '100', 
         'pageNo' : '1', 
         'sidoName' : '서울', 
         'ver' : '1.0' }

response = requests.get(url, params=params)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

c_item = soup.find_all('item')

for i in c_item :
    # 태그 글자 추출 => get_text() 또는 string
    print("stationName : " , i.select_one('stationName').string , end="\t")
    print("pm10Value : " , i.select_one('pm10Value').string , end="\t")
    print("pm25Value : " , i.select_one('pm25Value').string)
    
    # find 는 소문자로 해야 나옴
    #print("stationName : " , i.find('stationname').string , end="\t")
    #print("pm10Value : " , i.find('pm10value').string , end="\t")
    #print("pm25Value : " , i.find('pm25value').string)
    

    


