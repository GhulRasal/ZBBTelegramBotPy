import os
import telebot

BOT_TOKEN = "BotToken :)"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "Hola, cómo estas?")
    
bot.infinity_polling()