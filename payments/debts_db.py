import db
import datetime

#тут методы работы с базой данных
class DebtsDatabase():
    def __init__(self):
        db.check_db_exists()

    def set_debt(self, creditor_id=None, debtor_id=None, amount=None, message_id=""):
        db.insert(db.PAYMENTS_TABLE_NAME, {
            "creditor_id": creditor_id,
            "debtor_id": debtor_id,
            "amount": amount,
            "created": datetime.datetime.now(),
            "message_id": message_id,
            # add if list is extended
        })
        
    # заплатить одному пользователю денежку
    def payoff_debt(self, creditor_id=None, debtor_id=None, amount=None, message_id=""):
        # прочекать все ли ок
        # записать в базу данных
        # отправить сообщение (если бот может писать)
        pass

    # получить список должников
    def get_debtors(self, user_id=None):
        pass

    # получить список тех, кому должен
    def get_creditors(self, user_id=None):
        pass

    # узнать статус пользователя - сколько ты ему или он тебе должен + история операций
    def get_all_debts_user(self, current_user_id=None, request_user_id=None):
        #проверить задолженность конкретному пользователю
        pass

    def check_all(self):
        print(db.fetchall(db.PAYMENTS_TABLE_NAME, ["amount"]))