import telebot
from telebot import TeleBot, types
import sqlite3
import Pamail, Paria, Panek

bot = TeleBot(".**<<TOKEN>>**.")
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        cmd STRING,
        type STRING,
        town STRING,
        cfg STRING,
        id INTEGER)""")
    connect.commit()

    #check id
    u_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {u_id}")
    data = cursor.fetchone()
    if data is None:
        #add values
        user = [message.text, message.chat.type, "None", "None", message.from_user.id]
        cursor.execute("INSERT INTO login_id VALUES(?,?,?,?,?);", user)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Вы уже есть в базе данных!')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Hey there! I am a bit of a bot. Here are some of the commands: \n"
                                                    "/settings - настройки\n"
                                                    "/weather - выбор города, отображение погоды\n"
                                                    "/news - выбор категории, отображение новостей\n"
                                                    "/joke - отображение случайной шутки\n"
                                                    "/delete - удалить себя из базы данных\n")
@bot.message_handler(commands=['settings'])
def settings(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    print(message.text)
    u_id = message.chat.id
    cursor.execute(f"SELECT town FROM login_id WHERE id = {u_id}")
    town = str(cursor.fetchone())[2:-3]
    cursor.execute(f"SELECT cfg FROM login_id WHERE id = {u_id}")
    cfg = str(cursor.fetchone())[2:-3]
    connect.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Ваш город ("+town+")")
    btn2 = types.KeyboardButton("2. Категория новостей ("+cfg+")")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Что вы хотите настроить?', reply_markup=markup)
    bot.register_next_step_handler(message, setting)
def setting(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    print(message.text)
    if (message.text.count('1' or 'Город')):
        bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        bot.register_next_step_handler(message, settown)
    else:
        cursor.execute(f"UPDATE login_id SET cfg = 'None' WHERE id = {message.chat.id}")
        connect.commit()
        news(message)
        ##bot.register_next_step_handler(message, news)
@bot.message_handler(commands=['weather'])
def weather(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    u_id = message.chat.id
    cursor.execute(f"select cmd from login_id WHERE id={u_id}")
    cursor.execute(f"UPDATE login_id SET cmd = '{message.text[1:]}' WHERE id = {u_id}")
    cursor.execute(f"SELECT town FROM login_id WHERE id = {u_id}")
    connect.commit()
    town = str(cursor.fetchone())[2:-3]
    print(town)
    if town == "None":
        bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)')
        bot.register_next_step_handler(message, settown)
    else:
        bot.send_message(message.chat.id, Pamail.parse(town), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

def settown(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    print(message.text)
    u_id = message.chat.id
    cursor.execute(f"UPDATE login_id SET town = '{message.text}' WHERE id = {u_id}")
    cursor.execute(f"SELECT town FROM login_id WHERE id = {u_id}")
    connect.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Да")
    btn2 = types.KeyboardButton("2. Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Ваш город - ' + str(cursor.fetchone())[2:-3] + '?', reply_markup=markup)
    bot.register_next_step_handler(message, report)
def report(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT town FROM login_id WHERE id = {message.chat.id}")
    print(message.text)
    if (message.text.count('2' or 'Нет')):
        bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        bot.register_next_step_handler(message, settown)
    else:
        town = str(cursor.fetchone())[2:-3]
        bot.send_message(message.chat.id, Pamail.parse(town), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
@bot.message_handler(commands=['news'])
def news(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    u_id = message.chat.id
    cursor.execute(f"select cmd from login_id WHERE id={u_id}")
    cursor.execute(f"UPDATE login_id SET cmd = '{message.text[1:]}' WHERE id = {u_id}")
    cursor.execute(f"SELECT cfg FROM login_id WHERE id = {u_id}")
    connect.commit()
    cfg = str(cursor.fetchone())[2:-3]
    print(cfg)
    if cfg == "None":
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
        bot.send_message(message.chat.id, 'В какой категории хотите читать новости?', reply_markup=markup)
        bot.register_next_step_handler(message, newscat)
    else:
        bot.send_message(message.chat.id, Paria.parse(cfg), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
def newscat(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    u_id = message.chat.id
    cfgn = int(message.text.split('.')[0])-1
    cat = ['politics', 'world', 'economy', 'society', 'incidents','defense_safety','science','sport','culture','religion','tourism']
    print(cfgn,cat[cfgn])
    cursor.execute(f"UPDATE login_id SET cfg = '{cat[cfgn]}' WHERE id = {u_id}")
    cursor.execute(f"SELECT cfg FROM login_id WHERE id = {u_id}")
    connect.commit()
    cfg = str(cursor.fetchone())[2:-3]
    print(cfg)
    bot.send_message(message.chat.id, Paria.parse(cfg), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

@bot.message_handler(commands=['joke'])
def joke(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    u_id = message.chat.id
    cursor.execute(f"select cmd from login_id WHERE id={u_id}")
    cursor.execute(f"UPDATE login_id SET cmd = '{message.text[1:]}' WHERE id = {u_id}")
    connect.commit()
    bot.send_message(message.chat.id, Panek.parse(), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    u_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {u_id}")
    connect.commit()
    bot.send_message(message.chat.id, 'Вы успешно удалены из базы данных')

bot.polling()