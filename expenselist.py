from uuid import uuid4
class expense:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.id = str(uuid4)
    

    """ getter method """
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
        
    """ setter method """
    def set_value(self, x):
        self.name = x
    
    def set_name(self, y):
        self.value = y
