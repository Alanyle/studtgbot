from telebot import types
def settownkeys():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Да")
    btn2 = types.KeyboardButton("2. Нет")
    markup.add(btn1, btn2)
    return markup
def newscatkeys():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Политика")
    btn2 = types.KeyboardButton("2. В мире")
    btn3 = types.KeyboardButton("3. Экономика")
    btn4 = types.KeyboardButton("4. Общество")
    btn5 = types.KeyboardButton("5. Происшествия")
    btn6 = types.KeyboardButton("6. Армия")
    btn7 = types.KeyboardButton("7. Наука")
    btn8 = types.KeyboardButton("8. Спорт")
    btn9 = types.KeyboardButton("9. Культура")
    btn10 = types.KeyboardButton("10. Религия")
    btn11 = types.KeyboardButton("11. Туризм")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
    return markup
def settingskeys(town, cfg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Ваш город (" + town + ")")
    btn2 = types.KeyboardButton("2. Категория новостей (" + cfg + ")")
    markup.add(btn1, btn2)
    return markup