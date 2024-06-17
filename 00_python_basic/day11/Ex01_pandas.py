import pandas as pd
import numpy as np 

np.random.seed(101) # 같은 시드값지정하면 같은 랜덤값이 나온다.
# df = np.random.randn(5,4) # 5행 4열
data = np.random.randn(5,4) # 5행 4열
df = pd.DataFrame(data, columns=['W','X','Y','Z'] , index=['A','B','C','D','E'])
print(df)
print("**" * 50 )

# 데이터프레임 인덱싱 / 슬라이싱
print(df['W'], type(df['W']))  # 데이터프레임의 각 열은 시리즈 이다.
# print(df[1]) #인덱스 사용 못함
print("**" * 50 )

print(df[['W','Z']] , type(df[['W','Z']])) 
print("**" * 50 )

# 새로운 컬럼 추가
df['new'] = df['W'] + df['X']
print(df)

# 컬럼 삭제(.drop) 
print(df.drop('new', axis=1))
print(df) # 원본 삭제 되지 않은 상태

print(df.drop('new', axis=1, inplace=True ) )
print(df) # 원본 삭제 
print("**" * 50 )

# np.nan (결측치) = NaN 
df2 = pd.DataFrame({'A':[1,2,np.nan], 
                    'B':[5,np.nan,np.nan], 
                    'C':[1,2,3]})
print(df2)

m_cnt = df2.isnull().sum()
print("각 열의 결측치 개수 : {}" .format(m_cnt)) 
print("**" * 50 )

# 결측치를 포함하고 있는 모든 행 삭제 - dropna()
print(df2.dropna())
print("**" * 50 )

print(df2) # 원본 그대로
print("**" * 50 )

# 결측치를 포함하고 있는 모든 열 삭제 - dropna(axis=1) 
print(df2.dropna(axis=1))
print(df2) # 원본 그대로
print("**" * 50 )


# 결측치 대체 : fillna(value=)
print(df2.fillna(value=0))
print(df2)

# mean() : 산술평균
print(df2['A'].fillna(value=df2['A'].mean()))