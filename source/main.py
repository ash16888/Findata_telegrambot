# This is a simple  bot with financial information wich you can get in real time
import time
import telebot
import types
from yfin import price_now
from dict import *
import os
import random

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

###Bot
### Keyboard
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('SP500','Индекс РТС', 'Нефть BRENT')
keyboard1.row('USDRUB','Bitcoin', 'GOLD')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот который подскажет котировки в реальном времени. Мне нужен только тикер. Для акций РФ добавляем .ME  к примеру SВER.ME Используются данные  finance.yahoo.com', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Индекс РТС':
        bot.send_message(message.chat.id, price_now('RTSI.ME'))
    elif message.text == 'USDRUB':
        bot.send_message(message.chat.id, price_now('RUB=X'))
    elif message.text == 'Нефть BRENT':
        bot.send_message(message.chat.id, price_now('BZ=F'))
    elif message.text == 'Bitcoin':
        bot.send_message(message.chat.id, price_now('BTC-USD'))
    elif message.text == 'SP500':
        bot.send_message(message.chat.id, price_now('ES=F'))
    elif message.text == 'GOLD':
        bot.send_message(message.chat.id, price_now('GC=F'))
    else:
        bot.send_message(message.chat.id, price_now(find_key(d, message.text.lower())))
time.sleep(1)
