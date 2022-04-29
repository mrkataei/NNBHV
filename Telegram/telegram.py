from telebot import TeleBot
from time import sleep
from dotenv import load_dotenv


class TelegramInterface:
    def __init__(self, token: str = load_dotenv()):
        self.token = token
        self.bot = None
        self.user_dict = {}

    def bot_polling(self):
        print("Starting bot polling now")
        while True:
            try:
                print("New bot instance started")
                self.bot = TeleBot(self.token)  # Generate new bot instance
                self.bot_actions()  # If bot is used as a global variable, remove bot as an input param
                self.bot.polling(none_stop=True, interval=2, timeout=30)
            except Exception as ex:  # Error in polling
                print("Bot polling failed, restarting in {}sec. Error:\n{}".format(30, ex))
                self.bot.stop_polling()
                sleep(2)
            else:  # Clean exit
                self.bot.stop_polling()
            print("Bot polling loop finished")
            break  # End loop

    def bot_actions(self):
        raise Exception("NotImplementedException")


class TempBot(TelegramInterface):
    def __init__(self):
        TelegramInterface.__init__(self)

    def bot_actions(self):
        @self.bot.message_handler(func=lambda message: True)
        def excuse(message):
            self.bot.send_message(message.chat.id, ' 👷🏼‍♂️ ربات در حال تعمیر و بروزرسانی است.\n'
                                                   'از صبر و شکیبایی شما متشکریم! ')


class ClientBot(TelegramInterface):
    def __init__(self):
        super(ClientBot, self).__init__()

    def bot_actions(self):
        pass
