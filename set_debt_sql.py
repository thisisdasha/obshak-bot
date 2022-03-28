import db
from payments.debts_db import DebtsDatabase

#db._init_db()
test_db = DebtsDatabase()

def _test_set_pay():
    test_db.set_debt("000000", "000001", 500, 13)
    print(test_db.check_all())
    test_db.payoff_debt("000000", "000001", 300)
    test_db.get_creditors("000001")
    test_db.get_debtors("000000")
    test_db.get_all_debts_user("000000", "000001")
    test_db.get_all_debts_user("000001", "000000")

_test_set_pay()
