# tests/test_auth.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_user():
    payload = {
        "email": "newuser@example.com",
        "password": "password123"
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_login_user():
    payload = {
        "username": "newuser@example.com",
        "password": "password123"
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/auth/login", data=payload)

    assert response.status_code == 200
    assert "access_token" in response.json()
