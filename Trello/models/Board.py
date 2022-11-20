from models.User import User
from models.UniqueId import UniqueId
from models.Privacy import Privacy
from models.List import List
from exceptions.MissingKeyException import MissingKeyException
from collections import defaultdict
from typing import Iterable,cast

class Board(UniqueId):
    url_prefix="www.trello.org/"

    def __init__(self,name,privacy=Privacy.PUBLIC):
        super().__init__()
        self.__name=name
        self.__privacy=privacy
        self.__id=self.return_uuid()
        self.__url=self.url_prefix + self.__id
        self.__members=defaultdict(User)
        self.__lists=defaultdict(List)
    
    def show(self):
        return {
                "id": self.__id,
                "name": self.__name,
                "privacy": self.__privacy,
                "members": [user.show() for user in cast(Iterable[User],self.__members.values())]
                }

    def get_id(self):
        return self.__id 

    def create_list(self,name):
        l=List(name)
        self.__lists[l.get_id()]=l
        return l.get_id()

    def check_if_list_present(self,list_id):
        if list_id in self.__lists:
            return True
        else:
            raise MissingKeyException(list_id)

    def check_if_member_present(self,user_id):
        if user_id in self.__members:
            return True
        else:
            raise MissingKeyException(f"Member: {user_id}")            

    def get_list(self,list_id) -> List:
        if self.check_if_list_present(list_id):
            return self.__lists[list_id]

    def remove_list(self,list_id):
        if self.check_if_list_present(list_id):
            del self.__lists[list_id]
    
    def show_list(self,list_id):
        if self.check_if_list_present(list_id):
            self.__lists[list_id].show()

    def set_name(self,name):
        self.__name=name
    
    def set_privacy(self,privacy):
        self.__privacy=Privacy.type(privacy)
    
    def add_member(self,user:User):
        self.__members[user.get_id()]=user
    
    def remove_member(self,user:User):
        if self.check_if_member_present(user.get_id()):
            del self.__members[user.get_id()]


