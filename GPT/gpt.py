import openai
import telebot
import time

openai.api_key = "sk-proj-2CSdJUIzkUJrzHoayvxOT3BlbkFJ9qebwO4rNgPanAfZso59"

bot = telebot.TeleBot('6717179110:AAG-CutsCYamH-c32E5G1bcmrM7GSvXdpu0')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Отвечу на любой вопрос)')

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        messages = [{"role": "user", "content": message.text}]
        chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = chat_response['choices'][0]['message']['content']
        bot.send_message(message.chat.id, response)
        messages.append({"role": "assistant", "content": response})
    except openai.error.RateLimitError:
        bot.send_message(message.chat.id, "Превышен лимит запросов к API. Пожалуйста, подождите немного и попробуйте снова.")
        time.sleep(60)  # Задержка на 60 секунд

bot.polling(none_stop=True)
