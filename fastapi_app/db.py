from schema.item import Item
from typing import List

fake_db: List[Item] = [
    Item(id=1, name="tomato", description="red and round", prices=30),
    Item(id=2, name="potato", prices=15)
]