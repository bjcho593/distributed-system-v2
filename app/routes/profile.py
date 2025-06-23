from fastapi import APIRouter, HTTPException
from app.schemas import ProfileCreate, ProfileOut
from app.models import create_profile, get_profile_by_user_id

router = APIRouter()

@router.post("/", status_code=201)
def create(data: ProfileCreate):
    if get_profile_by_user_id(data.user_id):
        raise HTTPException(status_code=409, detail="Perfil ya existe")
    create_profile(data.dict())
    return {"message": "Perfil creado"}

@router.get("/{user_id}", response_model=ProfileOut)
def get(user_id: str):
    profile = get_profile_by_user_id(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return profile
