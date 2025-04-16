# tests/test_books.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_book(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "title": "Test Book",
        "author": "Test Author",
        "genre": "Fiction",
        "year_published": 2024
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/books/", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

@pytest.mark.asyncio
async def test_get_books(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/books/", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_generate_summary_for_book(auth_token, create_book):
    book_id = create_book["id"]
    headers = {"Authorization": f"Bearer {auth_token}"}

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(f"/api/v1/books/{book_id}/generate-summary", headers=headers)

    assert response.status_code == 200
    assert "summary" in response.json()
