class MissingKeyException(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return f"{self.value} is not present"

