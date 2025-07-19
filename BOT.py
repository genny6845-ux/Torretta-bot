import requests
from telegram import Bot

# Inserisci il tuo token e chat_id
TOKEN = "INSERISCI_IL_TUO_TOKEN"
CHAT_ID = "INSERISCI_IL_TUO_CHAT_ID"

bot = Bot(token=TOKEN)

def send_alert(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def check_portfolio():
    # Simulazione: qui puoi aggiungere la logica per leggere dati reali
    profitto = 750  # esempio statico
    if profitto >= 1000:
        send_alert("🔥 Obiettivo raggiunto: profitto > 1000€!")
    elif profitto < 0:
        send_alert("📉 Attenzione: portafoglio in perdita!")
    else:
        send_alert(f"📊 Profitto attuale: {profitto}€")

if __name__ == "__main__":
    check_portfolio()
