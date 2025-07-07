from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        
    def users_list(self):
        return self.repo.get_all()
    
    def create_user(self, name):
        if len(name) < 3:
            raise ValueError("Name too short")
        return self.repo.create(name)