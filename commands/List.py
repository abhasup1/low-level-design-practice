from services.BoardHandler import BoardHandler

class List:
    @staticmethod
    def parse_command_and_execute(board_handler:BoardHandler,command):
        if command[1]=="CREATE":
            board_id=command[2]
            name=command[3]
            board_handler.create_list(board_id,name)

        elif command[2]=="name":
            list_id=command[1]
            name=command[3]
            board_handler.set_list_name(list_id,name)
        
        elif command[1]=="DELETE":
            list_id=command[2]
            board_handler.remove_list(list_id)
