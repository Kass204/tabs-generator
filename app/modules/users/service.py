from app.modules.users.repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, db, data):
        return self.repository.create(
            db,
            name=data.name,
            email=data.email
        )

    def list_users(self, db):
        return self.repository.list(db)
