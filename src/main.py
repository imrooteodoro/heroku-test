from fastapi import FastAPI
from routes import router as test_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "heroku!"}

app.include_router(test_router)