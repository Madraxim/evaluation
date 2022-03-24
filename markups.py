from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_phone_number():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton(text='Поделитесь контактом!/ Kontaktni ulashish', request_contact=True)
    markup.add(btn)
    return markup

def generate_back_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton(text='◀️ Назад / ◀️Orqaga')
    markup.add(btn)
    return markup

def generate_admin_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    btn1 = KeyboardButton(text='Добавить коворкера')
    btn2 = KeyboardButton(text='Оценить коворкера')
    btn3 = KeyboardButton(text='Удалить коворкера')
    btn4 = KeyboardButton(text='''◀️ Назад / ◀️Orqaga''')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def generate_main_menu(coworkers):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []

    for coworker_name in coworkers:
        btn = KeyboardButton(text=coworker_name)
        buttons.append(btn)
    back = KeyboardButton(text='◀️ Назад / ◀️Orqaga')
    markup.add(*buttons, back)
    return markup


def generate_marks():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    buttons = []

    for mark in range(1, 6):
        btn = KeyboardButton(text=str(mark))
        buttons.append(btn)
    back = KeyboardButton(text='◀️ Назад / ◀️Orqaga')
    markup.add(*buttons, back)
    return markup