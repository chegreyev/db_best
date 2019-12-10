import telebot

token = '1001346113:AAGpu6jQbs3_F1YIIZ80aY7Yr0AD8RA0vco'

bot = telebot.TeleBot(token)
id = '451293803'

@bot.message_handler(commands = ['start'])
def start(message):
    while True:
        bot.send_message(message.from_user.id , 'это ддос САЛАМ')

if __name__ == "__main__":
    bot.polling()
    