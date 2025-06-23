from pydantic import BaseModel, EmailStr

class RecoveryRequest(BaseModel):
    email: EmailStr

class PasswordReset(BaseModel):
    token: str
    new_password: str
