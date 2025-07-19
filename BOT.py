from flask import Flask
import threading
import requests
import time
from telegram import Bot
import asyncio

app = Flask(__name__)

# Token e chat_id presi dalle variabili d’ambiente di Railway
import os
TOKEN = os.getenv("Token")
CHAT_ID = os.getenv("Chat_id")

bot = Bot(token=TOKEN)

async def send_alert(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        loop.run_until_complete(send_alert("🚨 Torretta attiva!"))
        time.sleep(600)  # ogni 10 minuti

@app.route("/")
def index():
    return "Bot attivo e pronto! 🚀"

if __name__ == "__main__":
    t = threading.Thread(target=start_bot)
    t.start()
    app.run(host="0.0.0.0", port=8080)
