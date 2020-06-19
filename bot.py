import telebot


bot = telebot.TeleBot("1174476779:AAE0zX3xf-ioir4agNdGiBHQFjObQZJBcqA")


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Давай начнём.\nПросто пришли номер блока.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
                b = int(message.text) * 0.0000004768371582
                i = float("{0:.9f}".format(b))
                bot.send_message(message.chat.id, str(i) + " GB")    
        except:
                bot.send_message(message.chat.id, "Умею отвечать только на число блоков!")
             
        
bot.polling(none_stop=True, interval=0)    
