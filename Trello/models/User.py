
class User():
    def __init__(self,name,id,email):
        self.__name=name
        self.__email=email 
        self.__id=id

    def get_id(self):
        return self.__id
    
    def show(self):
        return {
                "name": self.__name,
                "email": self.__email,
                "id": self.__id
                }