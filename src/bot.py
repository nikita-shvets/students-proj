import telebot
import asyncio
import requests
token=''


my_data = []

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    id = message.from_user.id
    name = message.from_user.username
    r = requests.post("http://localhost:8000/add_students", json={"tg_id": id, "tg_name": name})
bot.infinity_polling()
