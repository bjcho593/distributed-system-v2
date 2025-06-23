from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ProfileCreate(BaseModel):
    user_id: str
    name: str
    bio: Optional[str] = None
    email: EmailStr

class ProfileOut(BaseModel):
    user_id: str
    name: str
    bio: Optional[str] = None
    email: EmailStr
