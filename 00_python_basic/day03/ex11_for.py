# 데이터를 이용해서 합격자, 불합격자를 각각 저장하자
# 60 이상이면 합격

# 리스트
t_list = [90, 25, 67, 45, 80]

success = []
fail = []

for i in t_list :
    if i >= 60 :
        success.append(i)
    else : 
        fail.append(i)

print(success)
print(fail)

# 다른 방법
success2 = [ i for i in t_list if i >= 60]
fail2 = [ i for i in t_list if i < 60]
print(success2)
print(fail2)

# 튜플 => 불변형 자료형이므로 리스트로 형변환 후에 수정해야 한다.

print("ㅡ" * 30)

# 집합
t_set = {90, 25, 17, 49, 80}

success = set()
fail = set()

for i in t_set :
    if i >= 60 :
        success.add(i)
    else : 
        fail.add(i)

print(success)
print(fail)

print("ㅡ" * 30)

# 딕셔너리
t_dic = {
    "홍길동" : 90 ,
    "일지매" : 25 ,
    "장길산" : 67 ,
    "임꺽정" : 45 ,
    "홍법도" : 80
}

success = dict()
fail = dict()

for k, v in t_dic.items() :
    if v >= 60 :
        success[k] = v
    else : 
        fail[k] = v

print(success)
print(fail)

print("ㅡ" * 30)

success2 = dict()
fail2 = dict()

for i in t_dic.keys() :
    if t_dic[i] >= 60 :
        success2[i] = t_dic[i]
    else :
        fail2[i] = t_dic[i]

print(success2)
print(fail2)
