"""
    Mr.kataei
    update 2/22/2022
"""
from old.Inc import functions
from old import sleep, datetime, timedelta, telegram, config


_bot_ins = telegram.TeleBot(config('API_KEY'))


def delete_user_strategy(bot_ins):
    users = functions.get_users_validation_date()
    today = datetime.now()
    try:
        for user in users:
            valid_day = (user[1] - today).days
            if user[1] < today:
                functions.delete_all_user_strategies(username=user[0])
                bot_ins.send_message(chat_id=int(user[2]), text='your plan was expired!🥵\n'
                                                                'charge your /plan immediately')
                print(functions.set_is_valid_user(username=user[0]))
            elif user[1] < timedelta(days=1) + today:
                bot_ins.send_message(chat_id=int(user[2]), text=f'your plan will expired in {valid_day} day!🥵\n'
                                                                'charge your /plan immediately')
            elif user[1] < timedelta(days=2) + today:

                bot_ins.send_message(chat_id=int(user[2]), text=f'your plan will expired in {valid_day} days!🥵\n'
                                                                'charge your /plan immediately')
            elif user[1] < timedelta(days=3) + today:
                bot_ins.send_message(chat_id=int(user[2]), text=f'your plan will expired in {valid_day} days!🥵\n'
                                                                'charge your /plan immediately')
            elif user[1] < timedelta(days=4) + today:
                bot_ins.send_message(chat_id=int(user[2]), text=f'your plan will expired in {valid_day} days!🥵\n'
                                                                'charge your /plan immediately')
    except Exception as e:
        print(e)


def check_validate_stream():
    while True:
        delete_user_strategy(bot_ins=_bot_ins)
        sleep(28800)
