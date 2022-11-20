from collections import defaultdict
from models.Board import Board
from models.User import User
from models.Card import Card
from services.CardHandler import CardHandler
from exceptions.MissingKeyException import MissingKeyException

class ListHandler:
    def __init__(self):
        self.__lists_board_map=defaultdict(Board)
        self.__card_handler=CardHandler()
    
    def create_list(self,board:Board,list_name:str):
        list_id=board.create_list(list_name)
        self.__lists_board_map[list_id]=board
    
    def check_if_list_present(self,list_id):
        if list_id in self.__lists_board_map:
            return True
        else:
            raise MissingKeyException(list_id)

    def remove_list(self,list_id):
        if self.check_if_list_present(list_id):
            board:Board=self.__lists_board_map[list_id]
            board.remove_list(list_id)
            del self.__lists_board_map[list_id]
    
    def set_list_name(self,list_id,name):
        board:Board=self.__lists_board_map[list_id]
        list_obj=board.get_list(list_id)
        list_obj.set_name(name)

    def add_card(self,list_id,card_name):
        if self.check_if_list_present(list_id):
            board:Board=self.__lists_board_map[list_id]
            list_obj=board.get_list(list_id)
            self.__card_handler.add_card(list_obj,card_name)

    def get_board(self,list_id)->Board:
        if self.check_if_list_present(list_id):
            return self.__lists_board_map[list_id]
    
    def delete_card(self,card_id):
        self.__card_handler.delete_card(card_id)

    
    def move_card(self,card_id,destination_list_id):
        source_board:Board=self.get_board(self.__card_handler.get_list(card_id))
        dest_board:Board=self.get_board(destination_list_id)
        if source_board.get_id() == dest_board.get_id():
            dest_list_obj=dest_board.get_list(destination_list_id)
            self.__card_handler.move_card(dest_list_obj,card_id)
    
    def set_card_name(self,name,card_id):
        self.__card_handler.set_card_name(name,card_id)
    
    def set_card_desc(self,description,card_id):
        self.__card_handler.set_card_desc(description,card_id)

    def assign_card(self,card_id,user:User):
        card:Card=self.__card_handler.get_list(card_id).get_card(card_id)
        self.__card_handler.assign_card(card,user)

    def unassign_card(self,card_id):
        card:Card=self.__card_handler.get_list(card_id).get_card(card_id)
        self.__card_handler.unassign_card(card)

    def show_list(self,list_id):
        list_obj=self.get_board(list_id).get_list(list_id)
        print(list_obj.show())
    
    def show_card(self,card_id):
        self.__card_handler.show_card(card_id)
        




