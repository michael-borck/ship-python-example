"""Pydantic models for API request/response validation."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ItemBase(BaseModel):
    """Base item schema with common fields."""
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False


class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item (all fields optional)."""
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None


class Item(ItemBase):
    """Schema for item responses."""
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
