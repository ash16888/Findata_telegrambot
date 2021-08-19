# This is a simple  bot with financial information wich you can get in real time
import logging
import time
import flask
import telebot
import parse
import types 
import configparser
from yfin import price_now
from dict import *

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
API_TOKEN = config['Telegram']['API_TOKEN']
WEBHOOK_HOST = config['Telegram']['WEBHOOK_HOST']
WEBHOOK_PORT = config['Telegram']['WEBHOOK_PORT']
WEBHOOK_LISTEN =config['Telegram']['WEBHOOK_LISTEN']
WEBHOOK_SSL_CERT = config['Telegram']['WEBHOOK_SSL_CERT']
WEBHOOK_SSL_PRIV = config['Telegram']['WEBHOOK_SSL_PRIV']
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = flask.Flask(__name__)


# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

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

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
        debug=True)
