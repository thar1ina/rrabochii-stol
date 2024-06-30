import telebot
from telebot import types

bot = telebot.TeleBot('6804390299:AAFj0x5q5B0xQ5dTMmTCn7h2JpcBzyRQ0lI')  # Замените 'YOUR_TOKEN_HERE' на ваш токен

# Создание клавиатуры для сообщения 'start'
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1_menu = types.KeyboardButton('Меню')
markup.add(item1_menu)

# Клавиатура для главного меню
markup_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item2 = types.KeyboardButton('Платки')
item3 = types.KeyboardButton('Платья')
item4 = types.KeyboardButton('Кофты')
item5 = types.KeyboardButton('Юбки')
markup_main_menu.row(item2, item3, item4, item5)  # Добавляем кнопки в одну строку

# Клавиатура для подменю (для выбора юбок)
markup_skirts_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item_back = types.KeyboardButton('Назад')
item_skirt1 = types.KeyboardButton('Мини-юбки')
item_skirt2 = types.KeyboardButton('Миди-юбки')
item_skirt3 = types.KeyboardButton('Макси-юбки')
markup_skirts_menu.row(item_back)
markup_skirts_menu.row(item_skirt1, item_skirt2, item_skirt3)

# Словарь для отслеживания состояния чата
chat_state = {}

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Нажмите на кнопку для перехода по ссылке:", reply_markup=markup_main_menu)
    chat_state[chat_id] = 'main_menu'  # Установка начального состояния

# Обработчик нажатий кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id in chat_state:
        if chat_state[chat_id] == 'main_menu':
            if text == 'Юбки':
                bot.send_message(chat_id, "Выберите тип юбок:", reply_markup=markup_skirts_menu)
                chat_state[chat_id] = 'skirts_menu'
        elif chat_state[chat_id] == 'skirts_menu':
            if text == 'Назад':
                bot.send_message(chat_id, "Возвращаемся в главное меню", reply_markup=markup_main_menu)
                chat_state[chat_id] = 'main_menu'

bot.polling()
