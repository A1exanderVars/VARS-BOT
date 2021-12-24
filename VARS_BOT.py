import telebot
from telebot import types

#926615086:AAHUl8OG-xpenaOLNwj70O3BCXlqPULCAls

name = 'Игрок'
surname = 'Без регистрации'
age = 0
pol = "Не указано"
bal = 0
Телефон = "Не имеиться"
Одежда = "Не имеиться"
Автомобиль = "Не имеиться"
Dom = 'Не имеиться'

bot = telebot.TeleBot("5056196549:AAEzt-_7MF0Uxz9_Tc6obdyfNQDdAfCxWbg")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "🔥Добро пожаловать на\n🤖VARS BOT\nℹ️Что бы зарегестрироваться в боте пропишите команду\n\"Регистрация\"\nℹ️Что бы посмотреть мои команды введите мою команду\n\"Помощь\"")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Мешок':
        bot.reply_to(message, 'Вы успешно перенесли мешок и получили 10.000$')
        bot.register_next_step_handler(message,meshok )
    if message.text == 'Работать':
        bot.reply_to(message, '🔨Что бы работать, нужно ввести команду\n🔨\"Мешок\"')
    if message.text == 'Чит':
        bot.reply_to(message, '😊Введите сколько вам нужно стредств на баланс : ')
        bot.register_next_step_handler(message,cheat )
    if message.text == 'Магазин':
        bot.reply_to(message, '🏬Добро пожаловать в магазине VARS BOT\n📱Телефоны\n👔Одежда\n🚘Машины\n🏠Дом')
    if message.text == 'Б':
        bot.reply_to(message, '💵Твой кашелёк  : ' + str(bal) + '$')
    if message.text == 'Помощь':
        bot.reply_to(message, '📕Вот мои команды...\n👤Профиль\n💰Б [Баланс]\n🏬Магазин\n🔨Работать\n🏦Банк')
    elif message.text == 'Профиль':
        bot.reply_to(message, '👤Твой профиль.....\n👽Твой никнейм  : ' + name + "\n🎃Твой позывной  : "  + surname + "\n👥Твой пол  : " + pol +  "\n🔒Твой возраст  : " + str(age) + ' лет!' + '\n💵Твой кашелёк  : ' + str(bal) + '$'  + "\n📱Твой телефон : " + Телефон + "\n👔Твоя одежда : " + Одежда + "\n🚘Твой Автомобиль : " + Автомобиль + "\n🏠Твой дом : " + Dom)
    elif message.text == 'Дома':
        keyboard = types.InlineKeyboardMarkup()
        Яма = types.InlineKeyboardButton(text='🏠Яма', callback_data='Яма')
        keyboard.add(Яма)
        Дом1этаж = types.InlineKeyboardButton(text='🏠Дом[1этаж]', callback_data='Дом[1этаж]')
        keyboard.add(Дом1этаж)
        Дом2этаж = types.InlineKeyboardButton(text='🏠Дом[2этаж]', callback_data='Дом[2этаж]')
        keyboard.add(Дом2этаж)
        Дом3этаж = types.InlineKeyboardButton(text='🏠Дом[3этаж]', callback_data='Дом[3этаж]')
        keyboard.add(Дом3этаж)
        По_Дома = "Какой дом будем покупать?\n🏠Яма\n🏠Дом[1этаж]\n🏠Дом[2этаж]\n🏠Дом[3этаж]"
        bot.send_message(message.from_user.id, text = По_Дома, reply_markup=keyboard)
        
    elif message.text == 'Регистрация':
        bot.send_message(message.from_user.id, "🆘Добро пожаловать на регестрацию\n😎Введите свой никнейм  :")
        bot.register_next_step_handler(message, reg_name)
    elif message.text == 'Машины':
        keyboard = types.InlineKeyboardMarkup()
        ВАЗ_2106 = types.InlineKeyboardButton(text='🚘ВАЗ-2106', callback_data='ВАЗ-2106')
        keyboard.add(ВАЗ_2106)
        LADA_2114 = types.InlineKeyboardButton(text='🚘LADA 2114', callback_data='LADA 2114')
        keyboard.add(LADA_2114)
        Mersedes_Benz_AMG = types.InlineKeyboardButton(text='🚘Mersedes-Benz AMG', callback_data='Mersedes-Benz AMG')
        keyboard.add(Mersedes_Benz_AMG)
        BMW_M3 = types.InlineKeyboardButton(text='🚘BMW M3', callback_data='BMW M3')
        keyboard.add(BMW_M3)
        Porshe_gt3 = types.InlineKeyboardButton(text='🚘Porshe gt3', callback_data='Porshe gt3')
        keyboard.add(Porshe_gt3)
        Машины1 = "Какую машину будем брать?\n🚘ВАЗ-2106\n🚘LADA 2114\n🚘Mersedes-Benz AMG\n🚘BMW M3\n🚘Porshe gt3"
        bot.send_message(message.from_user.id, text = Машины1, reply_markup=keyboard)
    elif message.text == 'Одежда':
        keyboard = types.InlineKeyboardMarkup()
        Бомжа = types.InlineKeyboardButton(text='👔Бомжа', callback_data='Бомжа')
        keyboard.add(Бомжа)
        FILA = types.InlineKeyboardButton(text='👔FILA', callback_data='FILA')
        keyboard.add(FILA)
        PUMA = types.InlineKeyboardButton(text='👔PUMA', callback_data='PUMA')
        keyboard.add(PUMA)
        ADIDAS = types.InlineKeyboardButton(text='👔ADIDAS', callback_data='ADIDAS')
        keyboard.add(ADIDAS)
        NIKE = types.InlineKeyboardButton(text='👔NIKE', callback_data='NIKE')
        keyboard.add(NIKE)
        GUCCI = types.InlineKeyboardButton(text='👔GUCCI', callback_data='GUCCI')
        keyboard.add(GUCCI)
        Одежда1 = "Какого пашива одежду будем брать?\n👔Бомжа\n👔FILA\n👔PUMA\n👔ADIDAS\n👔NIKE\n👔GUCCI"
        bot.send_message(message.from_user.id, text = Одежда1, reply_markup=keyboard)
    elif message.text == 'Телефоны':
        keyboard = types.InlineKeyboardMarkup()
        Nokia3310 = types.InlineKeyboardButton(text='📱Nokia 3310', callback_data='Nokia 3310')
        keyboard.add(Nokia3310)
        XiomiM3 = types.InlineKeyboardButton(text='📱Xiomi M3', callback_data='Xiomi M3')
        keyboard.add(XiomiM3)
        Galaxys21 = types.InlineKeyboardButton(text='📱Galaxy s21', callback_data='Galaxy s21')
        keyboard.add(Galaxys21)
        iphone6s = types.InlineKeyboardButton(text='📱iphone 6s', callback_data='iphone 6s')
        keyboard.add(iphone6s)
        iphone12pro = types.InlineKeyboardButton(text='📱iphone 12 pro', callback_data='iphone 12 pro')
        keyboard.add(iphone12pro)
        Телефоны = 'Какой телефон будем брать?\n📱Nokia 3310\n📱Xiomi M3\n📱Galaxy s21\n📱iphone 6s\n📱iphone 12 pro'
        bot.send_message(message.from_user.id, text = Телефоны, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Яма":
        if bal < 10000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🏠")
        elif bal >= 10000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе дом \"🏠Яма\"")
            bot.register_next_step_handler(call.message,dom_yama )
    if call.data == "Дом[1этаж]":
        if bal < 50000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🏠")
        elif bal >= 50000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе дом \"🏠Дом[1этаж]\"")
            bot.register_next_step_handler(call.message,dom_1этаж )
    if call.data == "Дом[2этаж]":
        if bal < 100000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🏠")
        elif bal >= 100000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе дом \"🏠Дом[2этаж]\"")
            bot.register_next_step_handler(call.message,dom_2этаж )
    if call.data == "Дом[3этаж]":
        if bal < 200000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🏠")
        elif bal >= 200000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе дом \"🏠Дом[3этаж]\"")
            bot.register_next_step_handler(call.message,dom_3этаж )
    if call.data == "ВАЗ-2106":
        if bal < 50000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🚘")
        elif bal >= 50000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе автомобиль  \"🚘ВАЗ-2106\"")
            bot.register_next_step_handler(call.message,avto_vaz )
    if call.data == "LADA 2114":
        if bal < 100000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🚘")
        elif bal >= 100000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе автомобиль  \"🚘LADA 2114\"")
            bot.register_next_step_handler(call.message,avto_lada )
    if call.data == "Mersedes-Benz AMG":
        if bal < 200000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🚘")
        elif bal >= 200000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе автомобиль  \"🚘Mersedes-Benz AMG\"")
            bot.register_next_step_handler(call.message,avto_mers )
    if call.data == "BMW M3":
        if bal < 350000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🚘")
        elif bal >= 350000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе автомобиль  \"🚘BMW M3\"")
            bot.register_next_step_handler(call.message,avto_bmw )
    if call.data == "Porshe gt3":
        if bal < 500000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств🚘")
        elif bal >= 500000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе автомобиль  \"🚘Porshe gt3\"")
            bot.register_next_step_handler(call.message,avto_porshe )
          
    if call.data == "Бомжа":
        if bal < 1000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 1000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔Бомжа\"")
            bot.register_next_step_handler(call.message,Одежда_Бомжа )
    if call.data == "FILA":
        if bal < 5000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 5000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔FILA\"")
            bot.register_next_step_handler(call.message,Одежда_FILA )
    if call.data == "PUMA":
        if bal < 10000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 10000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔PUMA\"")
            bot.register_next_step_handler(call.message,Одежда_PUMA )
    if call.data == "ADIDAS":
        if bal < 15000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 15000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔ADIDAS\"")
            bot.register_next_step_handler(call.message,Одежда_ADIDAS )
    if call.data == "NIKE":
        if bal < 10000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 10000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔NIKE\"")
            bot.register_next_step_handler(call.message,Одежда_NIKE )
    if call.data == "GUCCI":
        if bal < 50000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств👔")
        elif bal >= 50000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе одежду пошива \"👔GUCCI\"")
            bot.register_next_step_handler(call.message,Одежда_GUCCI )
    if call.data == "Nokia 3310":
        if bal < 5000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств")
        elif bal >= 5000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе телефон 📱Nokia 3310")
            bot.register_next_step_handler(call.message,Gesh_Nokia )
    if call.data == "Xiomi M3":
        if bal < 15000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств")
        elif bal >= 15000 :
            bot.send_message(call.message.chat.id, "✅Вы успешно купили себе телефон 📱Xiomi M3")
            bot.register_next_step_handler(call.message,Gesh_XiomiM3 )
    if call.data == "Galaxy s21":
        if bal < 35000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств")
        elif bal >= 35000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе телефон 📱Galaxy s21")
            bot.register_next_step_handler(call.message,Gesh_Galaxys21 )
    if call.data == "iphone 6s":
        if bal < 95000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств")
        elif bal >= 95000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе телефон 📱iphone 6s")
            bot.register_next_step_handler(call.message,Gesh_iphone6s )
    if call.data == "iphone 12 pro":
        if bal < 300000 :
            bot.send_message(call.message.chat.id, "😢У вас не хватает средств")
        elif bal >= 300000 :
            bot.reply_to(call.message, "✅Вы успешно купили себе телефон 📱iphone 12 pro")
            bot.register_next_step_handler(call.message,Gesh_iphone12pro )
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "😘Ну что ж...\n📷Добро пожаловать в боте VARS BOT")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "🤖VARS BOT\n🆘Решил что нужно повторить регистрацию")
        bot.send_message(call.message.chat.id, "🆘Добро пожаловать на регестрацию\n😎Введите свой никнейм  :")
        bot.register_next_step_handler(call.message, reg_name)

    
        

	#bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "😎Введите свой позывной  :")
    bot.register_next_step_handler(message, reg_surname)
    
        

        
def meshok(message):
    global bal
    bal = bal + 10000

def avto_vaz(message):
    global bal
    bal = bal - 50000
    global Автомобиль
    Автомобиль ="ВАЗ-2106"

def dom_yama(message):
    global bal
    bal = bal - 10000
    global Dom
    Dom ="Яма"

def dom_1этаж(message):
    global bal
    bal = bal - 50000
    global Dom
    Dom ="Дом[1этаж]"

def dom_2этаж(message):
    global bal
    bal = bal - 100000
    global Dom
    Dom ="Дом[2этаж]"

def dom_3этаж(message):
    global bal
    bal = bal - 200000
    global Dom
    Dom ="Дом[3этаж]"

def avto_lada(message):
    global bal
    bal = bal - 100000
    global Автомобиль
    Автомобиль ="LADA 2114"

def avto_mers(message):
    global bal
    bal = bal - 200000
    global Автомобиль
    Автомобиль ="Mersedes-Benz AMG"

def avto_bmw(message):
    global bal
    bal = bal - 350000
    global Автомобиль
    Автомобиль ="BMW M3"

def avto_porshe(message):
    global bal
    bal = bal - 5000000
    global Автомобиль
    Автомобиль ="Porshe gt3"
    
def cheat(message):
    global bal
    bal = bal + int(message.text)
    bot.reply_to("💶Ваш баланс успешно пополнен на " + str(int(message.text)))

def Gesh_iphone6s(message):
    global bal
    bal = bal - 95000
    global Телефон
    Телефон = "iphone 6s"

def Одежда_Бомжа(message):
    global bal
    bal = bal - 1000
    global Одежда
    Одежда = "Бомжа"

def Одежда_GUCCI(message):
    global bal
    bal = bal - 50000
    global Одежда
    Одежда = "GUCCI"

def Одежда_PUMA(message):
    global bal
    bal = bal - 10000
    global Одежда
    Одежда = "PUMA"

def Одежда_NIKE(message):
    global bal
    bal = bal - 15000
    global Одежда
    Одежда = "NIKE"

def Одежда_ADIDAS(message):
    global bal
    bal = bal - 15000
    global Одежда
    Одежда = "ADIDAS"

def Одежда_FILA(message):
    global bal
    bal = bal - 5000
    global Одежда
    Одежда = "FILA"

def Gesh_iphone12pro(message):
    global bal
    bal = bal - 300000
    global Телефон
    Телефон = "iphone 12 pro"

def Gesh_Nokia(message):
    global bal
    bal = bal - 5000
    global Телефон
    Телефон = "Nokia 3310"

def Gesh_Galaxys21(message):
    global bal
    bal = bal - 5000
    global Телефон
    Телефон = "Galaxy s21"

def Gesh_XiomiM3(message):
    global bal
    bal = bal - 15000
    global Телефон
    Телефон = "Xiomi M3"


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "😎Введите свой пол(Мужчина,Женщина)  :")
    bot.register_next_step_handler(message, reg_pol)

def reg_pol(message) :
    global pol
    pol = message.text
    bot.send_message(message.from_user.id, "😎А Сколько вам уже годиков?  :")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "❗️Ошибка,Вводите цыфрами пожалуйста!")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = "✅Твой никнейм  : " + name + "\n🔱Твой позывной  : " + surname + "\n👥Твой пол  : " + pol + "\n🔰Тебе уже  : " + str(age) + " лет!\n❓Правильно?"
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "😘Ну что ж...\n📷Добро пожаловать в боте VARS BOT \n ℹ️Что бы посмотреть мои команды введите мою команду\n\"Помощь\"")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "🤖VARS BOT\n🆘Решил что нужно повторить регистрацию")
        bot.send_message(call.message.chat.id, "🆘Добро пожаловать на регестрацию\n😎Введите свой никнейм  :")
        bot.register_next_step_handler(call.message, reg_name)













bot.infinity_polling()






