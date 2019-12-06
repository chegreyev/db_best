import telebot

token = '1031841787:AAFjBjg-A1tTL1ViS2ZOKS3X2WJqSGIO0YU'

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling()