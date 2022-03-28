import db
from payments.debts_db import DebtsDatabase

#db._init_db()
test_db = DebtsDatabase()

def _test_set_pay():
    print(test_db.check_all())

_test_set_pay()
