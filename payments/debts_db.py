import db
import datetime

#тут методы работы с базой данных
class DebtsDatabase():
    def __init__(self):
        db.check_db_exists()

    def set_debt(self, creditor_id=None, debtor_id=None, amount=None):
        if (db.debts_search_by_users(creditor_id, debtor_id) == ()):
            db.insert(db.PAYMENTS_TABLE_NAME, {
                "creditor_id": creditor_id,
                "debtor_id": debtor_id,
                "amount": amount,
                "created": datetime.datetime.now(),
                # add if list is extended
            })
        else:
            record = db.debts_search_by_users(creditor_id, debtor_id)
            print(record)
            print("OK! "+str(record))
            db.debts_update_amount(id=record[0], amount=record[3]+amount)
        
        
    # заплатить одному пользователю денежку
    def payoff_debt(self, creditor_id=None, debtor_id=None, amount=None, message_id=""):
        print("Payment: Executing PAYOFF")
        current_record = db.debts_search_by_users(creditor_id, debtor_id)
        if (current_record == ()):
            raise Exception("not found")
        if (current_record[3] < amount):
            raise Exception("Amount paied is more than needed")
        db.debts_update_amount(id=current_record[0], amount=current_record[3]-amount)

    # получить список должников
    def get_debtors(self, user_id=None):
        print("Payment: Executing Get Debtors")
        return db.debts_search_debtors_by_creditor(user_id)

    # получить список тех, кому должен
    def get_creditors(self, user_id=None):
        print("Payment: Executing Get Creditors")
        return db.debts_search_creditors_by_debtor(user_id)

    def check_all(self):
        self.set_debt("000000", "000001", 400)
        print(db.debts_get_info_by_id(1))
        self.payoff_debt("000000", "000001", 300)
        self.payoff_debt("000000", "000001", 0)
        print(db.debts_get_info_by_id(1))
        print(self.get_debtors("000000"))
        print(self.get_creditors("000001"))
