import telebot

import obratka
import obratka_rus
import obratka_kz

from telebot import types

token = '1031841787:AAFjBjg-A1tTL1ViS2ZOKS3X2WJqSGIO0YU'

# Language
eng = obratka
rus = obratka_rus
kz = obratka_kz



bot = telebot.TeleBot(token)

first_subject = ''
second_subject = ''
profession = ''
city = ''
university = ''
user_login = ''
user_password = ''
user_rating = ''


@bot.message_handler(commands = ['univer'])
def commanda(message):
    first_subjects = libr.getFirstSubjects()

    keyboard = types.ReplyKeyboardMarkup()
    
    for fs in first_subjects:
        keyboard.add(fs)

    bot.send_message(message.from_user.id , 'What was the first subject on the exam?' , reply_markup=keyboard)
    bot.register_next_step_handler(message , first)

def first(message):
    global first_subject
    first_subject = message.text

    second_subjects = libr.getSecondSubjects(first_subject)

    keyboard = types.ReplyKeyboardMarkup()
    
    for ss in second_subjects:
        keyboard.add(ss)
    
    bot.send_message(message.from_user.id , 'What was the second subject: ⬇︎' , reply_markup=keyboard)
    bot.register_next_step_handler(message , second)

def second(message):
    global second_subject , first_subject
    second_subject = message.text

    professions = libr.getProfessionsBySubjects(first_subject , second_subject)

    keyboard = types.ReplyKeyboardMarkup()

    for prof in professions:
        keyboard.add(prof)

    bot.send_message(message.from_user.id , 'Choose the profession you want from the list: ⬇︎' , reply_markup=keyboard)
    bot.register_next_step_handler(message , city_vybor)

def city_vybor(message):
    global profession
    profession = message.text

    cities = libr.getCitiesByProfession(profession)

    keyboard = types.ReplyKeyboardMarkup()

    for city in cities:
        keyboard.add(city)

    bot.send_message(message.from_user.id , 'Choose city : ⬇︎', reply_markup=keyboard)
    bot.register_next_step_handler(message , university_vybor)

def university_vybor(message):
    global city
    city = message.text

    universities = libr.getUniversityByCity(city)

    keyboard = types.ReplyKeyboardMarkup()

    for univer in universities:
        keyboard.add(univer) 

    bot.send_message(message.from_user.id , 'Choose the University: ⬇︎', reply_markup=keyboard)
    bot.register_next_step_handler(message , university_info)

def university_info(message):
    global university
    university = message.text

    info = libr.getUniversityInfo(university)

    keyboard = types.ReplyKeyboardMarkup()

    keyboard.add('1' , '2' , '3' , '4' , '5')
    keyboard.add('/univer')

    bot.send_message(message.from_user.id , info + '\n\nCongratulations! So please rate the university about given info\nYou must rate by tapping the number from 1 to 5 from keyboard' , reply_markup=keyboard)
    bot.register_next_step_handler(message , rating)

def rating(message):
    global user_rating , profession , university
    try:
        user_rating = message.text
    
        user_id = message.from_user.id
        libr.registerUserRating(user_id , profession , university , user_rating)

        bot.send_message(message.from_user.id , 'Your rating has been registered!\nThank you it will help us to give more relevant informations to the next users.')
    except Exception:
        bot.send_message(message.from_user.id , "Oops!Maybe you have been filled with string or something else...\nPlease fill that with numbers. Thank you!")
      
@bot.message_handler(commands = ['login'])
def loginUser(message):
    bot.send_message(message.from_user.id , 'Do you want to register ?\nSo, the fill the Email field below ↓\n')
    bot.register_next_step_handler(message , login)

def login(message):
    global user_login
    user_login = message.text 

    bot.send_message(message.from_user.id , 'The next one is Password field ↓')
    bot.register_next_step_handler(message , password)

def password(message):
    global user_password
    user_password = message.text

    user_id = int(message.from_user.id)

    obratka.registerUser(user_id , user_login , user_password)

    bot.send_message(message.from_user.id , "Yeah!!! You've been registered on our bot's service ! Soon you will get the something interesting...")

@bot.message_handler(commands = ['start'])
def help(message):
    info = "Hello everyone ! I'm the bot that gives you information about the University" 
    info += "\nYou need to start choosing the University by clicking on Telegrams's keyboard"
    info += "\ncommand /univer and following the instructions"
    info += "\nYou MUST choose the language of the bot by clicking on the second row"
    info += "\nGood luck !"

    # Telegrams Keyboard
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('/univer' , '/login')
    keyboard.add('/kz' , '/rus' , '/eng')

    bot.send_message(message.from_user.id , info , reply_markup=keyboard)

@bot.message_handler(commands = ['rus'])
def change_lang(message):
    global rus , libr

    libr = rus

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('/univer')

    bot.send_message(message.from_user.id , 'Вы поменяли язык на русский' , reply_markup=keyboard)

@bot.message_handler(commands = ['kz'])
def change_lang(message):
    global kz , libr

    libr = kz

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('/univer')

    bot.send_message(message.from_user.id , 'Вы поменяли язык на казахский' , reply_markup=keyboard)

@bot.message_handler(commands = ['eng'])
def change_lang(message):
    global eng , libr

    libr = eng

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('/univer')

    bot.send_message(message.from_user.id , 'Вы поменяли язык на английский' , reply_markup=keyboard)

if __name__ == "__main__":
    print('Bot has been started')
    bot.polling()