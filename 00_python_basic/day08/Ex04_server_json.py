from urllib.request import urlopen
import json

myurl = "https://raw.githubusercontent.com/paullabkorea/coronaVaccinationStatus/main/data/data.json"
response = urlopen(myurl)

data = json.load(response)

for i in data :
    print(i['시·도별(1)'], end="  ")    
    print(i['총인구 (명)'], end="  ")    
    print(i['1차 접종 누계'], end="  ")    
    print(i['2차 접종 누계'], end="  ")    
    print('{:.1f}%' .format(i['1차 접종 퍼센트']), end="  ")
    print('{:.1f}%' .format(i['2차 접종 퍼센트']))
    






