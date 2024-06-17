# BeautifulSoup : HTML 및 XML 파일에서 데이터를 추출하기 위해 사용되는 파이썬 라이브러리
#                 크롤링 하기 위해 필요하다.

# 설치 : pip install beautifulsoup4

from bs4 import BeautifulSoup

# html 을 데려올때 파일을 읽어도 되고
# urllib 또는 request 를 이용하여 웹에서 소스를 가져와도 된다.

# 1.
# html 파일 읽기
with open('day07/sample.html', 'r', encoding='utf-8') as f1 :
    # html.parser 는 파이썬과 함께 제공되는 기본 파서
    soup = BeautifulSoup(f1, "html.parser")
print(soup)
    
print("ㅡ" * 30)

# 2.
# 파서 이용하기
with open('day07/sample.html', 'r', encoding='utf-8') as f2 :
    soup = BeautifulSoup(f2, "html.parser")
    # 해당 파일에 있는 모든 div 
    all_div = soup.find_all('div')
print(all_div, type(all_div))
    
print("ㅡ" * 30)

with open('day07/sample.html', 'r', encoding='utf-8') as f3 :
    soup = BeautifulSoup(f3, "html.parser")
    # 해당 파일에 있는 첫번째 div 만
    one_div = soup.find('div')
print(one_div, type(one_div))

print("ㅡ" * 30)

with open('day07/sample.html', 'r', encoding='utf-8') as f4 :
    soup = BeautifulSoup(f4, "html.parser")
    # 해당 파일에 있는 h1 만
    one_h1 = soup.find('h1')
print(one_h1)

print("ㅡ" * 30)





