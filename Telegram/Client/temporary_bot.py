from Interfaces.telegram import Telegram

# master bot already run on vps dont use this @aitrdbot -> address
# API_KEY = '2123917023:AAFPy9xoaJLt0BxqQJgC3J3F9km8F7ozdn8'
# @testkourosh2bot -> address // use this bot for test your code
# API_KEY = '1978536410:AAE_RMk3-4r_cLnt_nRcEnZHaSp-vIk9oVo'


class TempBot(Telegram):
    def __init__(self):
        Telegram.__init__(self)

    def bot_actions(self):
        @self.bot.message_handler(func=lambda message: True)
        def excuse(message):
            self.bot.send_message(message.chat.id, ' 👷🏼‍♂️ ربات در حال تعمیر و بروزرسانی است.\n'
                                                   'از صبر و شکیبایی شما متشکریم! ')


class Telegram:
    def __init__(self, API_KEY: str = config('API_KEY')):
        self.API_KEY = API_KEY
        self.bot = None
        self.user_dict = {}

    def bot_polling(self):
        print("Starting bot polling now")
        while True:
            try:
                print("New bot instance started")
                self.bot = telegram.TeleBot(self.API_KEY)  # Generate new bot instance
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