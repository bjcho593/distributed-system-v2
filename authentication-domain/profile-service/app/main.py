from fastapi import FastAPI
from app.routes import profile
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(profile.router, prefix="/profile")
