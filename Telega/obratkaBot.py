import telebot
import obratka
from telebot import types

token = '1031841787:AAFjBjg-A1tTL1ViS2ZOKS3X2WJqSGIO0YU'

bot = telebot.TeleBot(token)

first_subject = ''
second_subject = ''
profession = ''
city = ''
university = ''
user_login = ''
user_password = ''
rating = 0  

@bot.message_handler(commands = ['univer'])
def commanda(message):
    first_subjects = obratka.getFirstSubjects()

    keyboard = types.ReplyKeyboardMarkup()
    
    for fs in first_subjects:
        keyboard.add(fs)

    bot.send_message(message.from_user.id , 'Какой был первый предмет на ЕНТ' , reply_markup=keyboard)
    bot.register_next_step_handler(message , first)

def first(message):
    global first_subject
    first_subject = message.text

    second_subjects = obratka.getSecondSubjects(first_subject)

    keyboard = types.ReplyKeyboardMarkup()
    
    for ss in second_subjects:
        keyboard.add(ss)
    
    bot.send_message(message.from_user.id , 'Какой был второй предмет' , reply_markup=keyboard)
    bot.register_next_step_handler(message , second)

def second(message):
    global second_subject , first_subject
    second_subject = message.text

    professions = obratka.getProfessionsBySubjects(first_subject , second_subject)

    keyboard = types.ReplyKeyboardMarkup()

    for prof in professions:
        keyboard.add(prof)

    bot.send_message(message.from_user.id , 'Выбери профессию' , reply_markup=keyboard)
    bot.register_next_step_handler(message , city_vybor)

def city_vybor(message):
    global profession
    profession = message.text

    cities = obratka.getCitiesByProfession(profession)

    keyboard = types.ReplyKeyboardMarkup()

    for city in cities:
        keyboard.add(city)

    bot.send_message(message.from_user.id , 'Выбери город', reply_markup=keyboard)
    bot.register_next_step_handler(message , university_vybor)

def university_vybor(message):
    global city
    city = message.text

    universities = obratka.getUniversityByCity(city)

    keyboard = types.ReplyKeyboardMarkup()

    for univer in universities:
        keyboard.add(univer) 

    bot.send_message(message.from_user.id , 'Вот и универы', reply_markup=keyboard)
    bot.register_next_step_handler(message , university_info)

def university_info(message):
    global university
    university = message.text

    info = obratka.getUniversityInfo(university)

    keyboard = types.ReplyKeyboardMarkup()

    keyboard.add('1' , '2' , '3' , '4' , '5' , '/univer')

    bot.send_message(message.from_user.id , info + '\n\nОцените униврситет по этим данным\nОценка от 1-5\nЧисленно - это обязательно' , reply_markup=keyboard)

    bot.register_next_step_handler(message , rating)

def rating(message):
    global rating , profession , university
    try:
        rating = int(message.text)
    
        user_id = message.from_user.id

        obratka.registerUserRating(user_id , profession , university , rating)
        # DEBUG USER ID
        print(str(user_id))
        bot.send_message(message.from_user.id , 'Ваша оценка зарегестрирована')
    except Exception:
        bot.send_message(message.from_user.id , 'Вы ввели неправильную оценку или в тексте\nВведите цифрой пожалуйста')
      
@bot.message_handler(commands = ['login'])
def loginUser(message):
    bot.send_message(message.from_user.id , 'Зарегестрироваться желаете ?\nОтлично введите свой логин: ')
    bot.register_next_step_handler(message , login)

def login(message):
    global user_login
    user_login = message.text 

    bot.send_message(message.from_user.id , 'Теперь пароль: ')
    bot.register_next_step_handler(message , password)

def password(message):
    global user_password
    user_password = message.text

    user_id = int(message.from_user.id)

    obratka.registerUser(user_id , user_login , user_password)

    bot.send_message(message.from_user.id , 'Отлично теперь вы зарегестрированы')


if __name__ == "__main__":
    print('Bot has been started')
    bot.polling()