from models.UniqueId import UniqueId
from models.User import User

class Card(UniqueId):
    def __init__(self,name,description=None):
        super().__init__()
        self.__name=name
        self.__id=self.return_uuid()
        self.__description=description
        self.__assigned_user=None

    def get_id(self):
        return self.__id

    def assign_user(self,user:User):
        self.__assigned_user=user

    def unassign_user(self):
        self.__assigned_user=None
    
    def set_name(self,name):
        self.__name=name

    def set_description(self,description):
        self.__description=description
    
    def show(self):
        return {
                "id": self.__id,
                "name": self.__name,
                "description": self.__description,
                "assignedTo": self.__assigned_user
            }
    
