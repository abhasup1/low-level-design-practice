from services.BoardHandler import BoardHandler

class Show:
    @staticmethod
    def parse_command_and_execute(board_handler:BoardHandler,command):
        if len(command)==1:
            board_handler.show_all_boards()
        elif command[1]=="BOARD":
            board_id=command[2]
            board_handler.show_board(board_id)
        elif command[1]=="LIST":
            list_id=command[2]
            board_handler.show_list(list_id)
        elif command[1]=="CARD":
            card_id=command[2]
            board_handler.show_card(card_id)
