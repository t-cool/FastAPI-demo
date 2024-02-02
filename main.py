from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# リクエストデータのバリデーション用のモデルを定義
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# FastAPIインスタンスを作成
app = FastAPI()

# POSTリクエストのエンドポイントを定義
@app.post("/items/")
async def create_item(item: Item):
    # リクエストボディから受け取ったデータをそのまま返す（エコーバック）
    return {"item_name": item.name, "item_price": item.price}

animal_names = {
    1: "Lion",
    2: "Tiger",
    3: "Bear",
    4: "Giraffe",
    5: "Elephant",
    6: "Monkey",
    7: "Zebra",
    8: "Rabbit",
    9: "Panda"
}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    if item_id > 10:
        # item_idが10より大きい場合は、404エラーを返す
        raise HTTPException(status_code=404, detail="Item not found")
    elif 1 <= item_id <= 9:
        # item_idが1から9の場合
        return {"item_id": item_id, "q": animal_names[item_id]}
    else:
        # それ以外の場合
        return {"item_id": item_id, "q": q}

