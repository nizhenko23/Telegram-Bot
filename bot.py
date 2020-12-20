import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!".format(message.from_user, bot.get_me()))
@bot.message_handler(content_types=['text'])
def parrot(message):
    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)