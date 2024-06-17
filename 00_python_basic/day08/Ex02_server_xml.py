from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "http://www.kma.go.kr/XML/weather/sfc_web_map.xml"
response = urlopen(myurl)
soup = BeautifulSoup(response, "html.parser")

c_local = soup.find_all('local')
for i in c_local :
    print("도시:" , i.string , end="\t")
    print("날씨:" , i['desc'] , end="\t")
    print("온도:" , i['ta'])











