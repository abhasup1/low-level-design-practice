from collections import defaultdict
from models.Board import Board
from models.Privacy import Privacy
from models.Card import Card
from services.ListHandler import ListHandler
from services.UserHandler import UserHandler
from exceptions.MissingKeyException import MissingKeyException

from models.User import User

class BoardHandler:

    def __init__(self,user_handler:UserHandler):
        self.__boards=defaultdict(Board)
        self.__list_handler=ListHandler()
        self.__user_handler=user_handler
    
    def check_if_board_exists(self,board_id):
        if board_id in self.__boards:
            return True
        else:
            raise MissingKeyException(f"Board: {board_id}")

    def create_board(self,name,privacy=Privacy.PUBLIC):
        b=Board(name,privacy)
        self.__boards[b.get_id()]=b

    def delete_board(self,board_id):
        if self.check_if_board_exists(board_id):
            del self.__boards[board_id]

    def set_board_name(self,board_id,name):
        # print("entered function")
        if self.check_if_board_exists(board_id):
            b:Board = self.__boards[board_id]
            # print(f"Board is : {vars(b)}")
            b.set_name(name)
            # print(f"Board is after: {vars(b)}")

    
    def set_board_privacy(self,board_id,privacy):
        if self.check_if_board_exists(board_id):
            b:Board = self.__boards[board_id]
            b.set_privacy(privacy)
    
    def add_member(self,board_id,user_id):
        board:Board=self.__boards[board_id]
        user=self.__user_handler.get_user(user_id)
        board.add_member(user)

    def remove_member(self,board_id,user_id):
        board:Board=self.__boards[board_id]
        user=self.__user_handler.get_user(user_id)
        board.remove_member(user)

    def create_list(self,board_id,list_name):
        board=self.__boards[board_id]
        self.__list_handler.create_list(board,list_name)
    
    def remove_list(self,list_id):
        self.__list_handler.remove_list(list_id)
    
    def set_list_name(self,list_id,name):
        self.__list_handler.set_list_name(list_id,name)

    def add_card(self,list_id,card_name):
        self.__list_handler.add_card(list_id,card_name)
    
    def delete_card(self,card_id):
        self.__list_handler.delete_card(card_id)

    def move_card(self,card_id,dest_list_id):
        self.__list_handler.move_card(card_id,dest_list_id)
    
    def set_card_name(self,name,card_id):
        self.__list_handler.set_card_name(name,card_id)
    
    def set_card_desc(self,description,card_id):
        self.__list_handler.set_card_desc(description,card_id)
    
    def assign_card(self,card_id,user_id):
        user:User=self.__user_handler.get_user(user_id)
        self.__list_handler.assign_card(card_id,user)
    
    def unassign_card(self,card_id):
        self.__list_handler.unassign_card(card_id)
    
    def show_all_boards(self):
        all_boards_info=[]
        for board in self.__boards.values():
            board:Board=board
            all_boards_info.append(board.show())

        if len(all_boards_info)==0:
            print("No boards")
        else:
            print(all_boards_info)
    
    def show_board(self,board_id):
        board:Board=self.__boards[board_id]
        print(board.show())
    
    def show_list(self,list_id):
        self.__list_handler.show_list(list_id)
    
    def show_card(self,card_id):
        self.__list_handler.show_card(card_id)
    
