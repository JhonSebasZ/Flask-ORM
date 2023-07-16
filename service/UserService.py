from db import db
from models.User import User
from flask_marshmallow import Marshmallow
ma = Marshmallow()

class UserService:
    def create_user(self,username:str, email:str)->User:
        user:User = User(username, email)
        db.session.add(user)
        db.session.commit()
        return user

    def list_users(self):
        return db.session.execute(db.select(User).order_by(User.username)).scalars()
    
    def find_by_id(self, id:int):
        return db.get_or_404(User,id)
    
    def update(self, user:User):
        update_user:User = db.get_or_404(User,user.id)

        update_user.username = user.username
        update_user.email = user.email
        db.session.add(update_user)
        db.session.commit()
        return update_user
    
    def delete(self, id:int):
        delete_user:User = db.get_or_404(User,id)
        db.session.delete(delete_user)
        db.session.commit()
        return delete_user

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')

users_schema = UserSchema(many=True)
user_schema = UserSchema()