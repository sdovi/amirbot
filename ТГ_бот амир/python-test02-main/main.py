import telebot
from pymongo import MongoClient
import re
from config import TOKEN
from time import sleep
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

cluster = MongoClient('mongodb+srv://sdovi:820722zz@cluster0.j4mfvwp.mongodb.net/?retryWrites=true&w=majority')
db = cluster['DB']
collection = db['Info']
bot = telebot.TeleBot(TOKEN)

user_info = {
    "_id": None,
    "name": None,
    "phone": None
}

text = {
    'welcome': "Привет, Выберите язык,\n"
               "Салом, тилни танланг"
}

btn = {
    "btn_uz": KeyboardButton(text="Uz"),
    "btn_ru": KeyboardButton(text="Русс"),
}

inline_btn = dict({})  # инлайн кнопки
actions = dict({})  # ответы бота


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(btn['btn_uz'], btn['btn_ru'])
    bot.send_message(message.chat.id, text['welcome'], reply_markup=kb)


@bot.message_handler(content_types=['text'])
def main_func(message):
    if message.text == "Uz" or message.text == "Русс":
        language_down(message)


def language_down(message):  # выбор языка
    global text01, btn1, actions1, inline_btn1
    if message.text == "Uz":
        from text_uz import text01, btn1, actions1, inline_btn1
        user_info["_id"] = message.chat.id
    elif message.text == "Русс":
        from text_ru import text01, btn1, actions1, inline_btn1
        user_info["_id"] = message.chat.id

    text.update(text01)
    btn.update(btn1)
    actions.update(actions1)
    inline_btn.update(inline_btn1)

    kb = ReplyKeyboardMarkup(resize_keyboard=True)  # отправка запросов
    kb.add(btn['btn1'])
    user_choice = bot.send_message(message.chat.id, text['actions'], reply_markup=kb)
    bot.register_next_step_handler(user_choice, regist)


def regist(message):
    if message.text == "Регистрация":
        user_choise = bot.send_message(message.chat.id, "Отправьте имя", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(user_choise, regist_name)


def regist_name(message):
    user_info["name"] = message.text
    kna = ReplyKeyboardMarkup(resize_keyboard=True)  # принимает имя
    kna.add(btn['btn3'])
    bot.send_message(message.chat.id, "Отлично!", reply_markup=ReplyKeyboardRemove())
    user_choise = bot.send_message(message.chat.id, "Теперь напишите свой Телефоный номер В виде 998XXXXXXXXX\n"
                                                    "Или нажмите на кнопку⬇️", reply_markup=kna)
    bot.register_next_step_handler(user_choise, regist_phone)


def regist_phone(message):
    if message.content_type == 'contact':
        user_info['phone'] = int(message.contact.phone_number)  # принимает номер
        bot.send_message(message.chat.id, "Отлично", reply_markup=ReplyKeyboardRemove())
        kb = InlineKeyboardMarkup(row_width=1)
        for x, i in inline_btn.items():
            kb.add(i)
        sleep(1)
        bot.send_message(message.chat.id, "Успешно прошли регистрацию")
        bot.send_message(message.chat.id, text["caruz"], reply_markup=kb)
    elif len(message.text) == 12 and re.match(r'^(998)[\d]{9}$', message.text):
        user_info['phone'] = message.text  # принимает номер
        bot.send_message(message.chat.id, "Отлично", reply_markup=ReplyKeyboardRemove())
        kb = InlineKeyboardMarkup(row_width=1)
        for x, i in inline_btn.items():
            kb.add(i)
        sleep(1)
        bot.send_message(message.chat.id, "Успешно прошли регистрацию")
        bot.send_message(message.chat.id, text["caruz"], reply_markup=kb)
    else:
        bot.send_message(message.chat.id, "Не правильно")


@bot.callback_query_handler(func=lambda call: True)
def direction(call):
    chose_inline = int(call.data.split('_')[0])
    if chose_inline == 1:
        print("helll")
        bot.register_next_step_handler(direction, chose)
    elif chose_inline == 2:
        print("asd")
    elif chose_inline == 3:
        print('gae')


def chose(message):
    bot.send_message(message.chat.id, "asd")


def deteling(message):
    bot.send_message(message.chat.id, "asd12")


def contact(message):
    bot.send_message(message.chat.id, "asd321")


bot.polling()
