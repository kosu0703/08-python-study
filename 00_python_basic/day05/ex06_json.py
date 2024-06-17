import json
from collections import OrderedDict

group_data = OrderedDict()
albums = OrderedDict()

group_data['name'] = '여자친구'
group_data['members'] = ['소원', '예린', '은하', '유주', '신비', '엄지']

albums['EP 1집'] = 'Season of Glass'
albums['EP 2집'] = 'Flower Bud'
albums['EP 3집'] = 'Snowflake'
albums['정규 1집'] = 'LOL'
albums['EP 4집'] = 'THE AWAKENING'

group_data['albums'] = albums

# 출력
print(json.dumps(group_data, ensure_ascii=False, indent='\t'))

# json 파일로 저장하기
with open("day05/data/sample2.json" , 'w' , encoding='utf-8') as f :
    json.dump(group_data, f , ensure_ascii=False, indent='\t')

# 다른방법
with open("day05/data/sample3.json" , 'w' , encoding='utf-8') as f2 :
    f2.write(json.dumps(group_data, ensure_ascii=False, indent='\t'))
    
