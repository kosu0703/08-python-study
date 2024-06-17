import pandas as pd

m_dict = [{'id':1010, 'name':'마루치', 'Java':89, 'Python':78, 'Flask':90},
          {'id':1230, 'name':'아라치', 'Java':96, 'Python':80, 'Flask':92},
          {'id':1902, 'name':'을불', 'Java':90, 'Python':74, 'Flask':90},
          {'id':2002, 'name':'창조리', 'Java':98, 'Python':88, 'Flask':94}]

df = pd.DataFrame(m_dict)
print(df)
print("-" * 100)

df["sum"] = df["Java"] + df["Python"] + df["Flask"]
print(df)
print("-" * 100)

df["avg"] = df["sum"] / 3
print(df)
print("-" * 100)

print("학점은 리스트에 담아서 나중에 추가하자")
hak = []
for i in df["avg"]:
    if i >= 90:
        hak.append("A")
    elif i >= 80:
        hak.append("B")
    elif i >= 70:
        hak.append("C")
    else:
        hak.append("F")
df["hak"] = hak
print(df)