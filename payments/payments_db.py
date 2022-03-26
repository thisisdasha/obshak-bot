import db

#тут методы работы с базой данных
class PaymentsDatabase():
    def __init__(self):
        db._init_db()
        db.check_db_exists()

    def set_debt(self, request_user_id=None, debt_user_id=None, amount=None, message_id="", conf_id=""):
        # записать в базу данных
        # отправить сообщение (если бот может писать)
        pass
        
    # заплатить одному пользователю денежку
    def payoff_debt(self, debt_user_id=None, request_user_id=None, amount=None, message_id="", conf_id=""):
        # прочекать все ли ок
        # записать в базу данных
        # отправить сообщение (если бот может писать)
        pass

    # получить список должников
    def get_debtors(self, user_id=None):
        pass

    # получить список тех, кому должен
    def get_lenders(self, user_id=None):
        pass

    # узнать статус пользователя - сколько ты ему или он тебе должен + история операций
    def get_all_debts_user(self, user_id=None, request_user_id=None):
        #проверить задолженность конкретному пользователю
        pass

    # вернуть историю всех операций, связанных со мной
    def get_history(self, user_id):
        pass