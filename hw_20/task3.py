from task2 import Bot
from task1 import BotException


class TelegramBot(Bot):

    def __init__(self, name, url=None, chat_id=None):
        self.url = url
        self.chat_id = chat_id
        super().__init__(name)

    def set_url(self, url: str) -> None:
        self.url = url

    def set_chat_id(self, chat_id: str) -> None:
        self.chat_id = chat_id

    def send_message(self, message: str) -> str:
        if self.url is None or self.chat_id is None:
            raise BotException
        else:
            return f'{self.name} says {message} to  {self.chat_id} using {self.url}'

my_bot = TelegramBot("Marvin")
# my_bot.send_message("test") # raises exception BotException

print(my_bot.chat_id == None) # True
print(my_bot.url == None) # True
#
my_bot.set_chat_id("12345")
# my_bot.send_message("test") # raises exception BotException
#
my_bot.set_url("https://some.url.com")
print(my_bot.send_message("test"))