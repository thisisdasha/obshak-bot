import os
import logging
import obshak
import exceptions
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboardButton
from vk_api.utils import get_random_id, sjson_dumps

# GROUP_ID = os.getenv("VK_GROUP_ID")
# GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")

logging.basicConfig(level=logging.INFO)

GROUP_ID = '211937698'
GROUP_TOKEN = 'd71c0693eee4737b603bd4424ebd21b0cbd2280fcb5855b0cff5e62ca031dde1171d2563e727359a022ce'
API_VERSION = "5.131"

vk_session = vk_api.VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
long_poll = VkBotLongPoll(vk_session, GROUP_ID)


def send_message(peer_id, keyboard=None, message=''):
    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=message
    )


def add_custom_vkpay_keyboard():
    custom_keyboard = sjson_dumps({
        'one_time': False,
        'inline': True,
        'buttons': [[
            {'action': {
                'type': VkKeyboardButton.VKPAY.value,
                'payload': None,
                'hash': "action=pay-to-user&amount=333&user_id=340953279",
            }}
        ]]
    })
    return custom_keyboard


def start_long_polling():
    for event in long_poll.listen():
        # print(event.message.text)
        if event.type == VkBotEventType.MESSAGE_NEW:
            """Обрабатываем обычное сообщение"""
            peer_id = event.message.peer_id
            try:
                pass
                test_data = obshak.process_message(event.message.text.__str__())
            except exceptions.NotCorrectMessage as e:
                send_message(peer_id, add_custom_vkpay_keyboard(), 'Error')
                return
            send_message(peer_id, add_custom_vkpay_keyboard(),
                         f'Добавлен долг  {obshak.test_answer}')


if __name__ == '__main__':
    start_long_polling()
