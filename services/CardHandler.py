from models.Card import Card
from models.User import User
from models.List import List
from collections import defaultdict
from exceptions.MissingKeyException import MissingKeyException

class CardHandler:
    def __init__(self):
        self.__cards_list_map=defaultdict(List)
    
    def check_if_card_present(self,card_id):
        if card_id in self.__cards_list_map:
            return True
        else:
            raise MissingKeyException(f"Card: {card_id}")
    
    def add_card(self,list_obj:List,card_name):
        card=Card(card_name)
        list_obj.add_card(card)
        self.__cards_list_map[card.get_id()]=list_obj
    
    def delete_card(self,card_id):
        if self.check_if_card_present(card_id):
            list_obj:List=self.__cards_list_map[card_id]
            list_obj.remove_card(card_id)
            del self.__cards_list_map[card_id]
    
    def move_card(self,destination_list_obj:List,card_id):
        if self.check_if_card_present(card_id):
            source_list_obj:List=self.__cards_list_map[card_id]
            card=source_list_obj.get_card(card_id)
            destination_list_obj.add_card(card)
            source_list_obj.remove_card(card_id)
            self.__cards_list_map[card_id]=destination_list_obj

    def get_list(self,card_id)->List:
        if self.check_if_card_present(card_id):
            return self.__cards_list_map[card_id]

    def assign_card(self,card:Card,user:User):
        card.assign_user(user)
    
    def unassign_card(self,card:Card):
        card.unassign_user()
    
    def show_card(self,card_id):
        list_obj:List=self.get_list(card_id)
        card:Card=list_obj.get_card(card_id)
        print(card.show())
    
    def set_card_name(self,name,card_id):
        list_obj:List=self.get_list[card_id]
        card:Card=list_obj.get_card(card_id)
        card.set_name(name)
    
    def set_card_desc(self,description,card_id):
        list_obj:List=self.get_list(card_id)
        card:Card=list_obj.get_card(card_id)
        card.set_name(description)





