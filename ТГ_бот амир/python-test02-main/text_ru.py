from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

text01 = {
    "actions": "Вам нужно пройти регистрацию \n"
               "Нажмите на кнопку ниже",
    "management": f"Ректор: Далиев",
    "caruz": "Привет! \n"
             "Я бот по обслуживанию и ремонту Вашего автомобиля\n"
             "от компании: \n"
             "TOTAL автосервис и студии Детейлинга Car-Driver.  \n"
             "\n"
             "Я помогу Вам сделать расчёт ТО и подарю бесплатную консультацию или диагностику. \n"
             "\n"
             "👉Нажмите в ответном сообщении кнопку, соответствующую вашему запросу",
    "well_done": "Отлично!",
    "direction": "Выберите направление",
    "recall_send": "Ваш отзыв отправлен"
}

btn1 = {
    "btn1": KeyboardButton(text="Регистрация"),
    "btn2": KeyboardButton(text="Расписание"),
    "btn3": KeyboardButton(text='Отправьте номер', request_contact=True),
    "btn4": KeyboardButton(text="Информация о руководстве"),

}

inline_btn1 = {
    "btn_inline_1": InlineKeyboardButton(text='Связь с менеджером.', callback_data=1),
    "btn_inline_2": InlineKeyboardButton(text='Список детейлинг услуг', callback_data=2),
    "btn_inline_3": InlineKeyboardButton(text='Наши контакты и локации', callback_data=3)
}

actions1 = {
    "answer": "Расписание",
    "answer2": "Информация о руководстве",
    "answer3": "Оставить отзыв",

}