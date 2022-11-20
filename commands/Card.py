from services.BoardHandler import BoardHandler

class Card:
    @staticmethod
    def parse_command_and_execute(board_handler:BoardHandler,command):
        if command[1]=="CREATE":
            list_id=command[2]
            name=command[3]
            board_handler.add_card(list_id,name)
        elif command[2]=="name":
            card_id=command[1]
            name=command[3]
            board_handler.set_card_name(name,card_id)
        elif command[2]=="description":
            card_id=command[1]
            description=command[3]
            board_handler.set_card_desc(description,card_id)
        elif command[2]=="ASSIGN":
            card_id=command[1]
            user_id=command[3]
            board_handler.assign_card(card_id,user_id)
        elif command[2]=="MOVE":
            card_id=command[1]
            dest_list_id=command[3]
            board_handler.move_card(card_id,dest_list_id)
        elif command[2]=="UNASSIGN":
            card_id=command[1]
            board_handler.unassign_card(card_id)
