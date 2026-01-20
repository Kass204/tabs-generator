from sqlalchemy.orm import Session
from app.modules.login.models import Login

class LoginRepository:

    def create(self, db, data):
        login = Login(
            username=data.username,
            password=data.password,
            user_id=data.user_id
        )
        db.add(login)
        db.commit()
        db.refresh(login)
        return login


    def list(self, db: Session):
        return db.query(Login).all()
