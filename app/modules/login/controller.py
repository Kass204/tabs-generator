from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.modules.login.schemas import LoginCreate, LoginResponse
from app.modules.login.service import LoginService

router = APIRouter(prefix="/login", tags=["Login"])

service = LoginService()

@router.post("/", response_model=LoginResponse)
def create_login(Login: LoginCreate, db: Session = Depends(get_db)):
    return service.create_login(db, Login)

@router.get("/", response_model=list[LoginResponse])
def list_login(db: Session = Depends(get_db)):
    return service.list_Logins(db)
