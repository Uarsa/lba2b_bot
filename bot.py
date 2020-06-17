import telebot


bot = telebot.TeleBot("1174476779:AAE0zX3xf-ioir4agNdGiBHQFjObQZJBcqA")


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start','/rol')
        bot.send_message(message.from_user.id, "Давай начнём.\nПосто пришли номер блока.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
         if message.text == 'пока' or message.text == 'Пока':
                bot.send_message(message.chat.id, 'Успехов в новом году!')
         else:
                i = int(message.text) * 2
                bot.send_message(message.chat.id, i)
        
        
bot.polling(none_stop=True, interval=0)    
