from app.modules.login.repository import LoginRepository
from app.core.security import hash_password

class LoginService:
    def __init__(self):
        self.repository = LoginRepository()

    def create_login(self, db, data):
        payload = data.model_dump()
        payload["password"] = hash_password(data.password)
        return self.repository.create(db, payload)


    def list_login(self, db):
        return self.repository.list(db)
