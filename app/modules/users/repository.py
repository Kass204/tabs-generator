from sqlalchemy.orm import Session
from app.modules.users.models import User

class UserRepository:

    def create(self, db: Session, name: str, email: str):
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def list(self, db: Session):
        return db.query(User).all()
