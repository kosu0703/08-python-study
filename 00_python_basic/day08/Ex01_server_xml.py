# 서버로 가서 읽어오려면 urllib 가 필요하고
# 데이터를 읽기 위해서 beautifulSoup 이 필요

from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "http://localhost:8090/test05.do"
response = urlopen(myurl)
soup = BeautifulSoup(response, "html.parser")
#print(soup)

c_local = soup.find_all('local')
#c_local = soup.select('local')
for i in c_local :
    print("도시:" , i.string , end=" // ")
    # xml 에서 태그의 속성 가져오기 => ['속성명']
    print("날씨:" , i['desc'] , end=" // ")
    print("온도:" , i['ta'])











