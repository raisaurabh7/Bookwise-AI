import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_add_review(auth_token, create_book):
    book_id = create_book["id"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    review_data = {
        "book_id": book_id,
        "review_text": "Excellent read!",
        "rating": 4.5
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/reviews/", json=review_data, headers=headers)

    assert response.status_code == 200
    assert response.json()["review_text"] == "Excellent read!"

@pytest.mark.asyncio
async def test_get_reviews(auth_token, create_book_and_review):
    book_id = create_book_and_review["book_id"]
    headers = {"Authorization": f"Bearer {auth_token}"}

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/api/v1/reviews/{book_id}", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
