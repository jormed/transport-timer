from models.user_model import User, db

class UserRepository:
    def get_all(self):
        return User.query.all()
    
    def create(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user