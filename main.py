from typing import Optional
from fastapi import FastAPI

app = FastAPI()     # 建立一個 FAST API application
@app.get("/")       # 指定 api 路徑(get方法)
def read_root():
    return{"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
