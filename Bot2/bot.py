import telebot
from telebot import types
bot = telebot.TeleBot('6600758392:AAEQuoJ3MdC4iuFmYxdCKHyVuif5EPN0Ggg')

@bot.message_handler(commands=['start'])
def dollar(message):
    bot.reply_to(message, 'Напиши сумму и курс')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('USD/EUR', callback_data='usd/eur')
    item2 = types.KeyboardButton('EUR/USD', callback_data='eur/usd')
    item3 = types.KeyboardButton('USD/GBP', callback_data='usd/gbp')
    item4 = types.KeyboardButton('USD/GBP', callback_data='usd/gbp')

    markup.add(item1, item2, item3)

if __name__ == "__main__":
    bot.polling(none_stop=True)