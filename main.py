from fastapi import FastAPI
from database import Base, engine
from controllers.product_controller import router as product_router
from controllers.auth_controller import router as auth_router
from config import settings

app = FastAPI(
    title="Defense Point Products Catalog",
    description="Fast API Crud. First, you can authorize your credentials",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

Base.metadata.create_all(bind=engine)

app.include_router(product_router, tags=["Products"])
app.include_router(auth_router, tags=["Authentication"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)