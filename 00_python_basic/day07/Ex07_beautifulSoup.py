from bs4 import BeautifulSoup

# 태그와 속성을 이용해서 가져오기
# find('태그명', {'속성명' : '값', ...})

# div 에서 id 속성값이 sample_id 인 것만 가져오기
with open('day07/sample.html', 'r', encoding='utf-8') as f1 :
    soup = BeautifulSoup(f1, "html.parser")
    s1 = soup.find('div', {'id' : 'sample_id'})
print(s1)

print("ㅡ" * 30)

# div 에서 id 속성값이 sample_id 인 것 중에 p 태그만 가져오기
with open('day07/sample.html', 'r', encoding='utf-8') as f2 :
    soup = BeautifulSoup(f2, "html.parser")
    s2 = soup.find('div', {'id' : 'sample_id'})
    s3 = s2.find_all('p')
# 리스트로 저장된다.
print(s3) # [<p>stmt8</p>, <p>stmt7</p>, <p>stmt9</p>]

# 텍스트만 가져오기 (for문 사용)
for i in s3 :
    print(i.get_text())

print("ㅡ" * 30)






