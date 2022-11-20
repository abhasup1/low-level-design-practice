from models.User import User
from collections import defaultdict

class UserHandler:
    def __init__(self):
        self.__users=defaultdict(User)

    def create_user(self,name,user_id,email_id=None):
        user=User(name,user_id,email_id)
        self.__users[user_id]=user
    
    def get_user(self,user_id)->User:
        return self.__users[user_id]



