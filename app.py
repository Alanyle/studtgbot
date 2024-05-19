#DataBase tg.db management
import sqlalchemy
import user_table

#telegram bot
from telebot import TeleBot, types
from dotenv import load_dotenv
import os

#local files
import Pamail, Paria, Panek, check

User, session = user_table.user()
load_dotenv()
bot = TeleBot(os.getenv("TOKEN"))

print("bot is running on token ", os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    session.commit()
    #check id
    u_id = message.chat.id
    data = session.get(User, u_id)
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    print(str(session.query(User.cmd).filter(User.id == u_id).first()))
    print(data)
    if data is None:
        #add values
        user = User(cmd = message.text[1:], typ = message.chat.type, town = "None", cfg = "None", id = message.from_user.id)
        session.add(user)
        session.commit()
        bot.send_message(message.chat.id, 'Привет! Я добавил вас в свою базу данных! '
                                          'Можете написать /help чтобы узнать, что я умею.')
    else:
        bot.send_message(message.chat.id, 'Вы уже есть в базе данных!')
@bot.message_handler(commands=['help'])
def help(message):
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    print(str(session.query(User.cmd).filter(User.id == u_id).first()))
    bot.send_message(message.chat.id, "Вот вещи, которые я умею: \n"
                                                    "/settings - настройки\n"
                                                    "/weather - выбор города, отображение погоды\n"
                                                    "/news - выбор категории, отображение новостей\n"
                                                    "/joke - отображение случайной шутки\n"
                                                    "/delete - удалить себя из базы данных\n")
@bot.message_handler(commands=['settings'])
def settings(message):
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    print(str(session.query(User.cmd).filter(User.id == u_id).first()))
    town = str(session.query(User.town).filter(User.id == u_id).first())[2:-3]
    cfg = str(session.query(User.cfg).filter(User.id == u_id).first())[2:-3]
    session.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Ваш город ("+town+")")
    btn2 = types.KeyboardButton("2. Категория новостей ("+cfg+")")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Что вы хотите настроить?', reply_markup=markup)
    bot.register_next_step_handler(message, setting, u_id)
def setting(message, u_id):
    print(message.text)
    if (message.text.count('1' or 'Город')):
        bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        bot.register_next_step_handler(message, settown)
    else:
        session.query(User).filter_by(id=u_id).update({'cfg': "None"})
        news(message)
        ##bot.register_next_step_handler(message, news)
@bot.message_handler(commands=['weather'])
def weather(message):
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    session.commit()
    town = str(session.query(User.town).filter(User.id == u_id).first())[2:-3]
    print(town)
    if check.check(u_id) == True:
        if town == "None":
            bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)')
            bot.register_next_step_handler(message, settown)
        else:
            bot.send_message(message.chat.id, Pamail.parse(town), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, check.check(u_id))

def settown(message):
    print(message.text)
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'town': str(message.text)})
    town = str(session.query(User.town).filter(User.id == u_id).first())[2:-3]
    session.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Да")
    btn2 = types.KeyboardButton("2. Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Ваш город - ' + town + '?', reply_markup=markup)
    bot.register_next_step_handler(message, report)
def report(message):
    print(message.text)
    if (message.text.count('2' or 'Нет')):
        bot.send_message(message.chat.id, 'Введите свой город транслитом(например: omsk, moskva)', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
        bot.register_next_step_handler(message, settown)
    else:
        town = str(session.query(User.town).filter(User.id == message.chat.id).first())[2:-3]
        bot.send_message(message.chat.id, Pamail.parse(town), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
@bot.message_handler(commands=['news'])
def news(message):
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'cmd': 'news'})
    cfg = str(session.query(User.cfg).filter(User.id == message.chat.id).first())[2:-3]
    session.commit()
    print(cfg)
    if check.check(u_id) == True:
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
    else:
        bot.send_message(message.chat.id, check.check(u_id))

def newscat(message):
    u_id = message.chat.id
    cfgn = int(message.text.split('.')[0])-1
    cat = ['politics', 'world', 'economy', 'society', 'incidents','defense_safety','science','sport','culture','religion','tourism']
    print(cfgn,cat[cfgn])
    session.query(User).filter_by(id=u_id).update({'cfg': str(cat[cfgn])})
    cfg = str(session.query(User.cfg).filter(User.id == message.chat.id).first())[2:-3]
    session.commit()
    print(cfg)
    bot.send_message(message.chat.id, Paria.parse(cfg), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

@bot.message_handler(commands=['joke'])
def joke(message):
    u_id = message.chat.id
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    session.commit()
    if check.check(u_id) == True:
        bot.send_message(message.chat.id, Panek.parse(), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, check.check(u_id))

@bot.message_handler(commands=['delete'])
def delete(message):
    u_id = int(message.chat.id)
    data = session.get(User, u_id)
    session.query(User).filter_by(id=u_id).update({'cmd': str(message.text[1:])})
    print(session.query(User.cmd).filter_by(id=u_id).first())
    if data != None:
        x = session.query(User).filter_by(id=u_id).first()
        session.delete(x)
        session.commit()
        bot.send_message(message.chat.id, 'Вы успешно удалены из базы данных')
    else:
        bot.send_message(message.chat.id, 'Вас нет в базе! Чтобы удалить себя из базы, сначала добавьтесь в неё!')


bot.polling()