import datetime
import re
import exceptions
from model.debt_model import Debtor, Message
from payments.debts_db import DebtsDatabase

debts_db = DebtsDatabase()


def add_debtor(cred_id, debt_id, amount, msg):
    debts_db.add_debtor(Debtor(cred_id, debt_id, amount, datetime.datetime.now(), msg))


def get_debtors():
    pass


def get_creditors():
    pass


def pay():
    pass


def process_message(raw_message, creditor_id):
    """Парсит текст пришедшего сообщения о новом расходе."""
    print(raw_message)
    regexp_result = []
    try:
        # Регулярка выделяет id и сумму должника в сообщении.
        regexp_result = re.findall(r"(\d*)\|@\w+] (\d+)", raw_message)
    except AttributeError:
        print('Я не понял, соре(')
    if not regexp_result:
        raise exceptions.NotCorrectMessage(
            "Не могу понять сообщение. Напишите сообщение в формате, "
            "например:\n1500 метро")
    else:
        people = []
        amount = []
        text2 = []
        text = ''
        for i in regexp_result:
            text += 'ФИО:' + i[0] + ' Сумма:' + i[1] + '\n'
            text2.append('ФИО:' + i[0] + ' Сумма:' + i[1] + '\n')
            people.append(i[0])
            amount.append(i[1])
        print(people)
        print()
        print(amount)
    return Message(creditor_id, people, amount, text, text2)
