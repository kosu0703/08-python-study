# 최대값 구하기

# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자 중 가장 큰 값

def find_max(t_list) :
    n = len(t_list)     # 리스트에 입력된 매개변수 길이를 구하자
    max_v = t_list[0]   # 첫번째 값을 최대값으로 기억시킨다.
    
    for i in range(1, n) :      
        if t_list[i] > max_v :
            max_v = t_list[i]
            
    return max_v

t_list = [17, 92, 18, 32, 45, 68, 75]
print(find_max(t_list))

print("ㅡ" * 30)

# 두번이상 나온 이름 찾기

# 입력 : 이름이 n개 들어있는 리스트
# 출력 : 중복된 이름의 집합

def find_name(t_list2) :
    n = len(t_list2)
    res = set()
    
    for i in range(0, n-1) :
        for j in range(i+1, n) :
            if t_list2[i] == t_list2[j] :
                res.add(t_list2[i])
    
    return res
    
name = ['Tom', 'Jerry', 'Mike', 'Tom', 'hong', 'Mike']   
print(find_name(name))     

# 항목 추가 : list => append , set => add

print("ㅡ" * 30)

    
    