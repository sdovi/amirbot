from telebot.types import KeyboardButton, InlineKeyboardButton

text01 = {
    "actions": "Вам нужно пройти регистрацию \n"
               "Нажмите на кнопку ниже",
    "caruz": f"Привет! \n"
             "Я бот по обслуживанию и ремонту Вашего автомобиля\n"
             "от компании: \n"
             "'TOTAL автосервис и студии Детейлинга Car-Driver.'  \n"
             "\n"
             "Я помогу Вам сделать расчёт ТО и подарю бесплатную консультацию или диагностику. \n"
             "\n"
             "👉Нажмите в ответном сообщении кнопку, соответствующую вашему запросу ",
    "text1": "Регистрация",
    "text2": "Отправьте свое имя",
    "text3": "Супер!",
    "text4": "Теперь напишите свой Телефоный номер В виде 998XXXXXXXXX\n"
             "Или нажмите на кнопку⬇️",
    "text5": "Отлично",
    "text6": "Успешно прошли регистрацию",
    "text7": "Не правильно,\n"
             "Пройдите регистрацию заного",
    "text8": "1. Вы можете написать нашему менеджеру в тг  ⬇️\n"
             "Сюда  @Sdovi_money ✍️\n"
             "\n"
             "2 . Или позвонить по номеру \n"
             "<b>+998 90 085 61 99</b> ☎️",
    "text9": "<b>Хотите узнать стоимость выбранной услуги?</b> \n"
             "<b>Нажмите на кнопку ниже.</b>",
    "text10": "<b>Адрес филиал ТЛЗ:</b> \n"
              "\n"
              "г. Ташкент, Мирзо- Улугбекский р-н, ул. Саллар Буйи, дом 4 \n"
              "(напротив АЗС UZBEKNEFTEGAZ)\n"
              "<b>Мы на GOOGLE Картах:</b>\n"
              "https://maps.app.goo.gl/DpeKKcXjCTviJs4T8\n"
              "\n"
              "❇️   ❇️   ❇️   ❇️   ❇️   ❇️   ❇️\n"
              "\n"
              "<b>Адрес филиал Пойтахт:</b>\n"
              "\n"
              "г. Ташкент, Яшнабадский р-н, ул. Корасу, дом 28 (АЗС SUN \n"
              "PETROL-POYTAXT)\n"
              "<b>Мы на GOOGLE Картах:</b>:\n"
              "https://maps.app.goo.gl/DgH9tQHwfwEMhyfv6 \n"
              "\n"
              "❇️   ❇️   ❇️   ❇️   ❇️   ❇️   ❇️\n"
              "\n"
              "<b>Работаем ежедневно с 9.00 до 19.00</b>\n"
              "\n"
              "<b>Контактный телефон: </b>\n"
              "\n"
              "☎️ +998977239449 <b>ТЛЗ</b>\n"
              "☎️ +998930029449 <b>ПОЙТАХТ</b>\n"
              "\n"
              "🌐 www.car-driver.uz",
    "text11": "<b>Выберите класс своего автомобиля</b>",
    "text12": "Отлично",
    "text13": "Отлично",
    "text14": "Отлично",
    "text15": "Отлично",

}

btn1 = {
    "btn1": KeyboardButton(text="Регистрация"),
    "btn3": KeyboardButton(text='Отправьте номер', request_contact=True),

    "btn_inl_4": InlineKeyboardButton(text='1️⃣ - Express Полировка кузова', callback_data="4"),
    "btn_inl_5": InlineKeyboardButton(text='2️⃣ - Detailing Полировка', callback_data="5"),
    "btn_inl_6": InlineKeyboardButton(text='3️⃣ - Жидкое стекло', callback_data="6"),
    "btn_inl_7": InlineKeyboardButton(text='1️⃣ - группа A-B-C класс', callback_data="7"),
    "btn_inl_8": InlineKeyboardButton(text='2️⃣ - группа D-E класс', callback_data="8"),
    "btn_inl_9": InlineKeyboardButton(text='3️⃣ - группа F-S-S+-J класс', callback_data="9"),
    "btn_inl_10": InlineKeyboardButton(text='Назад', callback_data="10"),

}

inline_btn1 = {
    "btn_inline_1": InlineKeyboardButton(text='Связь с менеджером.', callback_data="1"),
    "btn_inline_2": InlineKeyboardButton(text='Список детейлинг услуг', callback_data="2"),
    "btn_inline_3": InlineKeyboardButton(text='Наши контакты и локации', callback_data="3"),
}

actions1 = {
}
