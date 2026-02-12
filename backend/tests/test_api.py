"""Tests for API endpoints."""

import pytest
from fastapi.testclient import TestClient

from my_app.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_items_empty(client):
    """Test listing items when empty."""
    response = client.get("/api/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_item(client):
    """Test creating an item."""
    item_data = {"title": "Test Item", "description": "A test item"}
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == item_data["title"]
    assert data["description"] == item_data["description"]
    assert "id" in data


def test_create_item_validation_error(client):
    """Test creating item with invalid data."""
    response = client.post("/api/items", json={"title": ""})
    assert response.status_code == 422


def test_get_item_not_found(client):
    """Test getting non-existent item."""
    response = client.get("/api/items/99999")
    assert response.status_code == 404
