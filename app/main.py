import os
import telebot

from models import Activity, get_activity_from_telegram_message
from crud import add
from service import get_response_for_successful_updating_of_activity

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, how can I help you?")

@bot.message_handler(commands=['pushup', 'pushups'])
def send_response(message):
    activity: Activity = get_activity_from_telegram_message(message)
    if activity:
        add(activity)
        response = get_response_for_successful_updating_of_activity(activity)
    else:
        response = "Invalid format. Please use '/pushup [amount]'."
    bot.reply_to(message, response)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def run_telegram_bot():
    bot.polling()

def main():
    print("Starting telegram bot, press Ctrl+C to stop.")
    run_telegram_bot()
    print("Ending telegram bot.")

if __name__ == '__main__':
    main()
