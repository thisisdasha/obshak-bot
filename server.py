import os
import logging
import obshak
import exceptions
import vk_api
import payments.payments as payments
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboardButton
from vk_api.utils import get_random_id, sjson_dumps

# GROUP_ID = os.getenv("VK_GROUP_ID")
# GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")

logging.basicConfig(level=logging.INFO)
payments = payments.Payments()

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

def start_long_polling():
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print("New message to bot: " + event.message.text)
            peer_id = event.message.peer_id
            send_message(peer_id, message=f'Мне прислали соообщение, пошел обрабатывать')

            try:
                test_data = obshak.process_message(event.message.text.__str__())
            except exceptions.NotCorrectMessage as e:
                send_message(peer_id,message='Я не понял, соре(')
            
            # если запрашивается оплата, пуляем кнопку в сообщении
            keyboard = payments.generate_VKpay_keyboard(100, payments.test_user_id)
            send_message(peer_id, keyboard, f'Kнопка оплаты')
            

if __name__ == '__main__':
    start_long_polling()
