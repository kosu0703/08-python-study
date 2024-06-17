# 한국 ICT 인재 개발원 정보
# https://ictedu.co.kr/index.php?main_page=home

from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://ictedu.co.kr/index.php?main_page=home"
response = urlopen(myurl)

soup = BeautifulSoup(response, "html.parser")
#print(soup)

c_title = soup.find_all('h3', {'class' : 'title'})
for i in c_title :
    print(i.find('a').string)
    
print("ㅡ" * 50)

c_lt = soup.find_all('li', {'class' : 'lt'})
for i in c_lt :
    print(i.find('div').string)

print("ㅡ" * 50)

# 두개 합치기 (두개 모두 가지고 있는 애를 찾자)
c_info = soup.find_all('div', {'class' : 'info'})
for i in c_info :
    """ 
    c_title = i.find_all('h3', {'class' : 'title'})
    c_lt = i.find_all('li', {'class' : 'lt'})
    
    for j in c_title :
        print(j.find('a').string.strip(), end=" // ")
    
    for j in c_lt :
        print(j.find('div').string.strip())
        
    """    
    
    # 한번에 사용
    c_title = i.find('h3', {'class' : 'title'}).find('a').string.strip()
    c_lt = i.find('li', {'class' : 'lt'}).find('div').string.strip()
    print(c_title , "//" , c_lt)
    
    print("ㅡ" * 50)


