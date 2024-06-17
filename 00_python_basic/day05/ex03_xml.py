import xml.etree.ElementTree as ET

tree = ET.parse("day05/data/xml_data.xml")

# xml 은 루트가 있다.
root = tree.getroot()

print("tag" , root.tag) # data 태그
print("attrib" , root.attrib)
print("text" , root.text)

print("ㅡ" * 30)

for i in root :
    print(i.tag, i.attrib, i.text) # student 태그

print("ㅡ" * 30)

for i in root.findall('student') :
    name = i.find('name').text
    age = i.find('age').text
    score = i.find('score').attrib # 여러개 => 딕셔너리로 나온다
    print(name , "\t" , age , "\t" , score)    

print("ㅡ" * 30)

# 데이타를 복사해와서 사용할때
data = """<?xml version="1.0"?>
<data>
    <student>
        <name>peter</name>
        <age>24</age>
        <score math="80" english="97"/>
    </student>
    <student>
        <name>elgar</name>
        <age>21</age>
        <score math="67" english="56"/>
    </student>
    <student>
        <name>hong</name>
        <age>36</age>
        <score math="76" english="81"/>
    </student>
</data>
"""

# str 을 xml 로 만들어서 파싱하기
root2 = ET.fromstring(data)
print(type(root2))

for i in root2.findall('student') :
    name = i.find('name').text
    age = i.find('age').text
    score = i.find('score').attrib 
    print(name , "\t" , age , "\t" , score)   

print("ㅡ" * 30)

# 리스트로 만들기
lis = []
for i in root2.findall('student') :
    name = i.find('name').text
    age = i.find('age').text
    score = i.find('score').attrib 
    lis.append(name)
    lis.append(age)
    lis.append(score)

print(lis)

print("ㅡ" * 30)










