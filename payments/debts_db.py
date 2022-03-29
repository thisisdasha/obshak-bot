import db
import datetime

# Тут методы работы с базой данных


class DebtsDatabase:
    def __init__(self):
        db.check_db_exists()

    def add_debtor(self, debtor):
        db.insert("obshak", {
            "creditor_id": debtor.cred_id,
            "debtor_id": debtor.debt_id,
            "amount": debtor.amount,
            "created_time": debtor.date_time,
            "raw_text": debtor.raw_text
        })

    # заплатить одному пользователю денежку
    def payoff_debt(self, creditor_id=None, debtor_id=None, amount=None):
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

    # тесты
    def check_all(self):
        self.set_debt("000000", "000001", 400)
        self.set_debt("000000", "000001", 400)
        self.set_debt("000000", "000001", 400)
        self.set_debt("000001", "000000", 400)
        print(db.debts_get_info_by_id(2))
        print(db.debts_get_info_by_id(1))
        self.set_debt("000000", "000001", 400)
        self.payoff_debt("000000", "000001", 300)
        self.payoff_debt("000000", "000001", 0)
        print(db.debts_get_info_by_id(1)[3] == 100)
        print(self.get_debtors("000000"))
        print(self.get_creditors("000001"))
