from services.BoardHandler import BoardHandler
from services.UserHandler import UserHandler
from commands.Board import Board
from commands.Card import Card
from commands.List import List
from commands.Show import Show

if __name__=="__main__":
    user_handler=UserHandler()
    user_handler.create_user("Ajay Singh","user-1","ajay@gmail.com")
    user_handler.create_user("Kajal Verma","user-2","kajal@gmail.com")
    user_handler.create_user("Ravi KK","user-3","ravi@gmail.com")
    board_handler=BoardHandler(user_handler)
    
    print("Starting infinite while loop..")
    while(True):
        command=input("Enter command:").split(" ")
        if command[0]=="SHOW":
            Show.parse_command_and_execute(board_handler,command)
        elif command[0]=="BOARD":
            Board.parse_command_and_execute(board_handler,command)
        elif command[0]=="LIST":
            List.parse_command_and_execute(board_handler,command)
        elif command[0]=="CARD":
            Card.parse_command_and_execute(board_handler,command)
    
        
        

            
            




