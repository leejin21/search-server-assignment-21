
class MainException(Exception):
    def __init__(self, msg):
        self.code = msg

class InvalidDataException(MainException):
    pass

class InvalidDBAcessException(MainException):
    pass
