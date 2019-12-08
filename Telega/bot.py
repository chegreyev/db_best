import telebot
import parser
from telebot import types

token = '1031841787:AAFjBjg-A1tTL1ViS2ZOKS3X2WJqSGIO0YU'

bot = telebot.TeleBot(token)
all = parser.get_all()

name = ''
surname = ''
city = ''
university = ''
profession = ''


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.from_user.id , 'Привет , давай знакомиться\nКак тебя зовут?')
    bot.register_next_step_handler(message , get_name)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id , "Хорошо {}, а фамилия ?".format(name))
    bot.register_next_step_handler(message , get_surname)

def get_surname(message):
    global name , surname
    surname = message.text
    bot.send_message(message.from_user.id , "Вот и познакомились\n{} {}".format(name , surname))

@bot.message_handler(commands = ['Univers'])
def showCities(message):
    global all
    cities = parser.getCities(all)
    # Keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)

    for city in cities:
        keyboard.add(city)

    bot.send_message(message.from_user.id , "Выбери город" , reply_markup=keyboard)
    bot.register_next_step_handler(message , getUniversFromCity)

def getUniversFromCity(message):
    global city
    city = message.text

    universities = parser.getUnivers(city)

    keyboardCity = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for univer in universities:
        keyboardCity.add(univer['university_name'])

    bot.send_message(message.from_user.id , "Выберите ВУЗ" , reply_markup=keyboardCity)
    bot.register_next_step_handler(message , getProfessions)

def getProfessions(message):
    global university , city

    university = message.text

    professions = parser.getProfessions(city , university)

    keyboardProfession = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for profession in professions:
        keyboardProfession.add(profession['prof_title'])

    bot.send_message(message.from_user.id , 'Выбери Профессию' , reply_markup=keyboardProfession)
    bot.register_next_step_handler(message , getSubjects)

def getSubjects(message):
    global profession , city , university

    profession = message.text

    subjects = parser.HUI(city , university , profession)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for pr in subjects:
        keyboard.add(pr)

    bot.send_message(message.from_user.id , 'Вот и уроки' , reply_markup= keyboard)



    
if __name__ == "__main__":
    bot.polling()