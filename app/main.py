from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.routes import auth, books, reviews
from app.database import create_db_and_tables

app = FastAPI(
    title="Bookwise AI",
    version="1.0.0",
    description="API for intelligent book management using LLaMA3",
    contact={
        "name": "Your Name",
        "email": "you@example.com"
    }
)

# Register routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(reviews.router, prefix="/api/v1/reviews", tags=["Reviews"])

# Run DB setup on app startup
@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

# 👇 Custom Swagger UI config to enable Bearer token input
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    # Apply BearerAuth to all secured routes
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Apply the custom OpenAPI config
app.openapi = custom_openapi
