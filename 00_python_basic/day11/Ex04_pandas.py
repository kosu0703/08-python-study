import pandas as pd

e_list = [[100,"이도", "CEO"],
          [110,"마루치", "IT_PROG"],
          [121,"홍길동", "IT_PROG"],
          [227,"둘리", "IT_PROG"],
          [247,"공실이", "MANAGE"],
          ]
s_name = ["empno", "name", "job_id"]

df = pd.DataFrame(e_list, columns=s_name)
print(df)
print("-" * 50)

# print(df["empno"])
# print(df.empno)

# empno 가 120이상인 사람의 정보
print(df[df["empno"] >= 120])
# print(df.query('empno>=120'))
print("-" * 50)

# empno가 200이상이면서 job_id가 'IT_PROG'인 사람
# print(df[(df["empno"] >= 200) & (df["job_id"] == "IT_PROG")])
print(df.query("empno>=200 and job_id == 'IT_PROG'"))
