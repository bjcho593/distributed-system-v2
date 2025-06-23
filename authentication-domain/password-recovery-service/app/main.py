from fastapi import FastAPI
from app.routes import recovery
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(recovery.router, prefix="/recovery")
