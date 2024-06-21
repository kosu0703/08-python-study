from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel) :
    id : int
    name : str
    price : float

items = [
    {"id" : 1, "name" : "apple", "price" : 5000},
    {"id" : 2, "name" : "banana", "price" : 4000},
    {"id" : 3, "name" : "mango", "price" : 6000}
]

# @ 를 파이썬에서는 데코레이션이라고 사용하는데 (자바의 어노테이션과 같은 말이다.)
@app.get("/")
def hello() :
    return 'Hello Fast_API'

# Fast API 에서 반환할 응답의 데이터 모델인 Item 객체들의 리스트 형식
@app.get("/items", response_model=List[Item])
def get_items() :
    return items

@app.post("/items", response_model=List[Item])
def add_item(item : Item):
    # 추가 전에 아이디 중복 체크
    items.append(item)
    return items

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')
