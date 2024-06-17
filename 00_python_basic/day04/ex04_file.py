# data 안에 있는 text01.txt 를 test01.txt 로 복사하자

f1 = open("day04/data/text01.txt" , 'r' , encoding='utf-8')
f2 = open("day04/data/test01.txt" , 'w' , encoding='utf-8')

# read() 가 한번에 끝내서 편하다
data = f1.read()
f2.write(data)

f2.close()
f1.close()

# test01.txt 에 데이터를 추가하자
f3 = open("day04/data/test01.txt" , 'a' , encoding='utf-8')

for i in range(6, 11) :
    data = "{}번째 줄 입니다.\n" .format(i)
    f3.write(data)

f3.close()


