import itertools

class UniqueId:
    def __init__(self):
        self.global_id=next(itertools.count())
    def return_uuid(self):
        return str(hash(f"{str(type(self))}{self.global_id}"))