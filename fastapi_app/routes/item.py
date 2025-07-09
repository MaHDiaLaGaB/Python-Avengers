from fastapi import APIRouter, HTTPException, status
from schema.item import Item
from db import fake_db

route = APIRouter()

@route.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            return item
        

@route.post("/items/create")
def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400)
    fake_db.append(item)
    return {"status": status.HTTP_201_CREATED}