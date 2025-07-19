from flask import Flask
import threading
import asyncio
import os
from telegram import Bot

app = Flask(__name__)

TOKEN = os.getenv("Token")
CHAT_ID = os.getenv("Chat_id")
bot = Bot(token=TOKEN)

async def send_alert():
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="🚨 Torretta attiva!")
            await asyncio.sleep(600)  # ogni 10 minuti
        except Exception as e:
            print(f"Errore durante invio messaggio: {e}")
            await asyncio.sleep(60)  # riprova dopo 1 minuto se errore

def start_async_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_alert())

@app.route("/")
def index():
    return "Bot attivo e funzionante! ✅"

if __name__ == "__main__":
    threading.Thread(target=start_async_loop).start()
    app.run(host="0.0.0.0", port=8080)
