class Bot:

    def __init__(self, name):
        self.name = name

    def send_message(self, message: str) -> str:
        return message

    def get_name(self) -> str:
        return self.name
