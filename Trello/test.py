import unittest
from services.BoardHandler import BoardHandler
from services.UserHandler import UserHandler

class TestCases(unittest.TestCase):
    def __init__(self,methodName:str=...)->None:
        super().__init__(methodName)
        self.user_handler=UserHandler()
        self.user_handler.create_user("Ajay Singh","user-1","ajay@gmail.com")
        self.user_handler.create_user("Kajal Verma","user-2","kajal@gmail.com")
        self.user_handler.create_user("Ravi KK","user-3","ravi@gmail.com")
        self.board_handler=BoardHandler(self.user_handler)
    
    def test_board_creation(self):
        try:
            self.board_handler.create_board("Board-1")
        except Exception as e:
            print(e)

if __name__=="__main__":
    unittest.main()
