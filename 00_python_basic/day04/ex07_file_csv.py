# CSV 파일에 with 사용하기

import csv

with open("day04/data/csv02.csv" , 'w' , encoding='utf-8' , newline='') as f1 :
    wr = csv.writer(f1)
    wr.writerow([1, 'hong' , 270 , 90])
    wr.writerow([2, 'kim' , 240 , 80])
    wr.writerow([3, 'pack' , 210 , 70])
    wr.writerow([4, 'cho' , 180 , 60])
    wr.writerow([5, 'ko' , 300 , 100])

with open("day04/data/csv02.csv" , 'r' , encoding='utf-8') as f2 :
    rd = csv.reader(f2)
    
    for i in rd :
        print(i)    

print("ㅡ" * 30)

lines = []
with open("day04/data/csv02.csv" , 'r' , encoding='utf-8') as f3 :
    rd = csv.reader(f3)
    
    for i in rd :
        if int(i[3]) >= 90 :
            i.append("A")
            i.append("우수자")
        elif int(i[3]) >= 80 :
            i.append("B")
        elif int(i[3]) >= 70 :
            i.append("C")
        else : 
            i.append("F")
        
        lines.append(i)    
    
with open("day04/data/csv02_e.csv" , 'w' , encoding='utf-8' , newline='') as f4 :
    wr = csv.writer(f4)
    wr.writerows(lines)
    
    
    
    
    
    
    