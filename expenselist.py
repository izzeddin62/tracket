from uuid import uuid4
class expense:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.id = str(uuid4)
    