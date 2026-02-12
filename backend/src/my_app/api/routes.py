"""API route definitions."""

from fastapi import APIRouter, HTTPException
from typing import List

from ..models.schemas import Item, ItemCreate, ItemUpdate

router = APIRouter()

# In-memory storage for demonstration
items_db: dict[int, Item] = {}
next_id = 1


@router.get("/items", response_model=List[Item])
async def list_items():
    """List all items."""
    return list(items_db.values())


@router.post("/items", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item."""
    global next_id
    new_item = Item(id=next_id, **item.model_dump())
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    stored_item = items_db[item_id]
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item.model_copy(update=update_data)
    items_db[item_id] = updated_item
    return updated_item


@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
