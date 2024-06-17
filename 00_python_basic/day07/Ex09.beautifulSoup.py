# 공공데이터 기상청 날씨 XML
# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1.
# 날씨 xml 읽기
target = urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")
#print(soup)

# 2.
# location 태그 찾기
for i in soup.select('location') :
    # 텍스트만 가져오기 => get_text() 대신 string 사용 가능
    print('도시 : ', i.select_one('city').get_text())
    print('날씨 : ', i.select_one('wf').string)
    print('최저 : ', i.select_one('tmn').string , '도')
    print('최고 : ', i.select_one('tmx').string , '도')
    print('ㅡ' * 20)




