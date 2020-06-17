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
        i = int(message.text) * 562
        bot.send_message(message.chat.id, i)
        
        '''   
        if type(message.text) == type(1):      
        else:
                bot.send_message(message.chat.id, "Умею отвечать только на число!")
        '''        
        
        '''
         if message.text == 'пока' or message.text == 'Пока':
                bot.send_message(message.chat.id, 'Успехов в новом году!')
         else:
                i = int(message.text) * 562.5
                bot.send_message(message.chat.id, i)
         '''       
        
        
bot.polling(none_stop=True, interval=0)    
