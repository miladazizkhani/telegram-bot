from telegram import Bot
import schedule
import time
import random

TOKEN = 'توکن_ربات_تو'
CHANNEL_ID = '@YourChannel'

bot = Bot(token=TOKEN)

morning_messages = ["☀️ صبح بخیر! روزت پر از انرژی 🌸"]
noon_messages = ["🍽️ ظهر بخیر! وقت استراحته 🌼"]
motivation_messages = ["امروز همون روزیه که می‌تونه همه چیزو تغییر بده 🔥"]
songs = ["https://t.me/YourChannel/123"]

def send_morning():
    bot.send_message(chat_id=CHANNEL_ID, text=random.choice(morning_messages))

def send_noon():
    bot.send_message(chat_id=CHANNEL_ID, text=random.choice(noon_messages))

def send_motivation():
    bot.send_message(chat_id=CHANNEL_ID, text=random.choice(motivation_messages))

def send_song():
    bot.send_message(chat_id=CHANNEL_ID, text=random.choice(songs))

schedule.every().day.at("08:00").do(send_morning)
schedule.every().day.at("12:00").do(send_noon)
schedule.every().day.at("15:00").do(send_motivation)
schedule.every().day.at("18:00").do(send_song)

while True:
    schedule.run_pending()
    time.sleep(10)
