import re
# import db
import datetime
from typing import List, NamedTuple, Optional

import exceptions


def process_message(raw_message):
    _parse_message(raw_message)
    return 'test_data'


def test_answer(message):
    pass


def _parse_message(raw_message):
    """Парсит текст пришедшего сообщения о новом расходе."""
    print(raw_message)
    # print(type(raw_message))
    # try:
    #     regexp_result = re.search(r"(\[id\d*)\|@\w+] (\d+) ", raw_message)
    # except AttributeError:
    #     print('test')
    #     regexp_result = re.match(r"(\[id\d*)\|@\w+] (\d+) ", raw_message)
    # print(regexp_result)
    # print(regexp_result.group(1).strip().lower())

    # if not regexp_result or not regexp_result.group(0) \
    #         or not regexp_result.group(1) or not regexp_result.group(2):
    #     raise exceptions.NotCorrectMessage(
    #         "Не могу понять сообщение. Напишите сообщение в формате, "
    #         "например:\n1500 метро")

    # amount = regexp_result.group(1).replace(" ", "")
    # category_text = regexp_result.group(2).strip().lower()
    # return Message(amount=amount, category_text=category_text)
