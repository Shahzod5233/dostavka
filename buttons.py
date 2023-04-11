from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Knopka dlya otpravki nomera telefona

def fhone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Podelitsya kontaktom',request_contact=True)

    kb.add(button)

    return kb

# Knopka dlya otpravki lokacii
def lokation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Podelitsya lokaciey',request_location=True)

    kb.add(button)

    return kb

# Knopka dlya vibora pola
def gendr_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Mujchina')
    button2 = KeyboardButton('Jenshina')

    kb.add(button, button2)

    return kb


# Knopka dlya korzini
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Ochistit')
    button2 = KeyboardButton('Oformit zakaz')
    button3 = KeyboardButton('Redaktirovat')
    button4 = KeyboardButton('Nazad')

    kb.add(button, button2,button3, button4,)

    return kb


# Knopki pri vibore sposoba oplati
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Nalichnie')
    button2 = KeyboardButton('Kartoy')
    button3 = KeyboardButton('Nazad')

    kb.add(button, button2, button3)

    return kb