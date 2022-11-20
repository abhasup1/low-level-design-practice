from models.UniqueId import UniqueId
from models.Card import Card
from collections import defaultdict
from exceptions.MissingKeyException import MissingKeyException
from typing import cast,Iterable

class List(UniqueId):
    def __init__(self,name):
        super().__init__()
        self.__name=name
        self.__id=self.return_uuid()
        self.__cards=defaultdict(Card)

    def get_id(self):
        return self.__id
    
    def set_name(self,name):
        self.__name=name

    def add_card(self,card:Card):
        self.__cards[card.get_id()]=card

    def check_if_card_present(self,card_id):
        if card_id in self.__cards:
            True
        else:
            raise MissingKeyException(f"Card: {card_id}")
    
    def remove_card(self,card_id):
        if self.check_if_card_present(self,card_id):
            del self.__cards[card_id]
    
    def get_card(self,card_id):
        if self.check_if_card_present(self,card_id):
            return self.__cards[card_id]
    
    def show(self):
        return {
                "id": self.__id,
                "name": self.__name,
                "cards": [card.show() for card in cast(Iterable[Card],self.__cards.values())]
            }
