import telebot

from app.crud import add
from app.service import get_response_for_successful_updating_of_activity
from app.models.telegram import Message
from app.models.activity import Activity
from app.models.utils import get_activity_from_telegram_message
from app.config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, "Hello, how can I help you?")

@bot.message_handler(commands=['pushup', 'pushups'])
def send_response(message: Message):
    activity: Activity = get_activity_from_telegram_message(message)
    if activity:
        add(activity)
        response: str = get_response_for_successful_updating_of_activity(activity)
    else:
        response: str = "Invalid format. Please use '/pushup [amount]'."
    bot.reply_to(message, response)

@bot.message_handler(func=lambda m: True)
def echo_all(message: Message):
    bot.reply_to(message, message.text)

def run_telegram_bot():
    bot.polling()
