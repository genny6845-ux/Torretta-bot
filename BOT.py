from flask import Flask
import threading
import requests
from telegram import Bot

# Dummy Flask app per Render
app = Flask(__name__)

# Inserisci il tuo token e chat_id
TOKEN = "INSERISCI_IL_TUO_TOKEN"
CHAT_ID = "INSERISCI_IL_TUO_CHAT_ID"

bot = Bot(token=TOKEN)

def send_alert(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def check_portfolio():
    # Simulazione: qui puoi aggiungere la logica vera
    profitto = 750  # esempio statico
    if profitto >= 500:
        send_alert(f"🚀 Profitto raggiunto: {profitto}$!")
    else:
        send_alert(f"📉 Profitto attuale: {profitto}$")

def start_bot():
    while True:
        check_portfolio()
        # Aspetta 10 minuti prima del prossimo controllo
        time.sleep(600)

# Avvia il bot in un thread separato
threading.Thread(target=start_bot).start()

@app.route('/')
def home():
    return "Torretta Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
