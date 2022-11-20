from services.BoardHandler import BoardHandler

class Board:
    @staticmethod
    def parse_command_and_execute(board_handler:BoardHandler,command):
        if command[1]=="CREATE":
            name=command[2]
            board_handler.create_board(name)
        elif command[1]=="DELETE":
            board_id=command[2]
            board_handler.delete_board(board_id)
        elif len(command)>3 and command[2]=="name":
            board_id=command[1]
            name=command[3]
            board_handler.set_board_name(board_id,name)
        elif len(command)>3 and command[2]=="privacy":
            board_id=command[1]
            privacy=command[3]
            board_handler.set_board_privacy(board_id,privacy)
        elif len(command)>3 and command[2]=="ADD_MEMBER":
            board_id=command[1]
            user_id=command[3]
            board_handler.add_member(board_id,user_id)
        elif len(command)>3 and command[2]=="REMOVE_MEMBER":
            board_id=command[1]
            user_id=command[3]
            board_handler.remove_member(board_id,user_id)
