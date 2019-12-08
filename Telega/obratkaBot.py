import telebot
import obratka
from telebot import types

token = '1031841787:AAFjBjg-A1tTL1ViS2ZOKS3X2WJqSGIO0YU'

bot = telebot.TeleBot(token)

first_subject = ''
second_subject = ''
profession = ''
city = ''

@bot.message_handler(commands = ['univer'])
def commanda(message):
    first_subjects = obratka.getFirstSubjects()

    keyboard = types.ReplyKeyboardMarkup()
    
    for fs in first_subjects:
        keyboard.add(fs)

    bot.send_message(message.from_user.id , 'Какой был первый предмет' , reply_markup=keyboard)
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




if __name__ == "__main__":
    bot.polling()