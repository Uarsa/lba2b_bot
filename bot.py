import telebot
from telebot import apihelper
from telebot.types import Message


bot = telebot.TeleBot("1174476779:AAE0zX3xf-ioir4agNdGiBHQFjObQZJBcqA")


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Давай начнём.\nПосто пришли номер блока.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
                i = int(message.text) * 562
                bot.send_message(message.chat.id, str(i) + " bytes")    
        except:
                bot.send_message(message.chat.id, "Умею отвечать только на число!")
            
        
        '''   
        if type(message.text) == type(1):      
        else:
                bot.send_message(message.chat.id, "Умею отвечать только на число!")
        '''        
        
        
        
        
bot.polling(none_stop=True, interval=0)    
