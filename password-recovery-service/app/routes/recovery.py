from fastapi import APIRouter, HTTPException
from app.schemas import RecoveryRequest, PasswordReset
from app.utils.token import generate_token

router = APIRouter()

@router.post("/request")
def request_recovery(data: RecoveryRequest):
    token = generate_token(data.email)
    return {"message": "Token generado", "token": token}

@router.post("/reset")
def reset_password(data: PasswordReset):
    # Aquí se validaría el token y se restablece la contraseña
    return {"message": "Contraseña actualizada"}
