import os
import json
import logging
import obshak
import exceptions
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

# GROUP_ID = os.getenv("VK_GROUP_ID")
# GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")

logging.basicConfig(level=logging.INFO)
GROUP_ID = '211937698'
GROUP_TOKEN = 'd71c0693eee4737b603bd4424ebd21b0cbd2280fcb5855b0cff5e62ca031dde1171d2563e727359a022ce'
API_VERSION = "5.131"

CALLBACK_TYPES = ("show_snackbar", "open_link", "open_app")

vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
long_poll = VkBotLongPoll(vk_session, GROUP_ID)


def send_message(peer_id, keyboard=None, message=''):
    vk.messages.send(
        peer_id=peer_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=message
    )


def make_keyboard(test_data, i):
    keyboard_1 = VkKeyboard(one_time=False, inline=True)
    keyboard_1.add_callback_button(
        label='Подтвердить',
        color=VkKeyboardColor.SECONDARY,
        payload={"type": 'show_snackbar-' + str(test_data.people[i]) + '-' + str(test_data.creditor),
                 'text': str(test_data.amount[i]) + ' ' + str(test_data.text2[i])
                 }
    )
    return keyboard_1.get_keyboard()


def confirm(event):
    obshak.add_debtor(event.object.payload.get('type').split('-')[1],
                      event.object.payload.get('type').split('-')[2],
                      event.object.payload.get('text').split(' ')[0],
                      event.object.payload.get('text').split(' ')[1])
    event.object.payload['type'] = str(event.object.payload['type']).split('-')[0]
    r = vk.messages.sendMessageEventAnswer(
        event_id=event.object.event_id,
        user_id=event.object.user_id,
        peer_id=event.object.peer_id,
        event_data=json.dumps(event.object.payload),
    )
    last_id = vk.messages.edit(
        peer_id=event.obj.peer_id,
        message=event.object.payload['text'],
        conversation_message_id=event.obj.conversation_message_id,
    )


def reject(event):
    r = vk.messages.sendMessageEventAnswer(
        event_id=event.object.event_id,
        user_id=event.object.user_id,
        peer_id=event.object.peer_id,
        event_data=json.dumps({
            'type': 'show_snackbar',
            'text': 'Вы не можете подтвердить задолженность за другого человека'
        }),
    )


def start_long_polling():
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print("New message to bot: " + event.message.text)
            peer_id = event.message.peer_id
            send_message(peer_id, message=f'Мне прислали соообщение, пошел обрабатывать')
            try:
                test_data = obshak.process_message(event.message.text.__str__(), event.message.from_id)
                for i in range(len(test_data.people)):
                    send_message(peer_id, make_keyboard(test_data, i), test_data.text2[i])
            except exceptions.NotCorrectMessage as e:
                send_message(peer_id, message='Я не понял, сори(')
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type').split('-')[0] in CALLBACK_TYPES:
                if str(event.object.user_id) == str(event.object.payload.get('type').split('-')[1]):
                    confirm(event)
                else:
                    reject(event)


if __name__ == '__main__':
    start_long_polling()
