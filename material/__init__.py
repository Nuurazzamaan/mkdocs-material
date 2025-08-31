import os
import requests
from flask import Flask, request
from telegram import Bot, Update, LabeledPrice
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# Telegram Bot Token
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TELEGRAM_TOKEN)6858738346:AAGK3Go9b0SbNYKBObIS9zljVTIU5aBE5XI

# Chapa API Key
CHAPA_API_KEY = "YOUR_CHAPA_SECRET_KEY"CHAPUBK_TEST-xfd4WrSjA8laIRkpGSdWn0mS4HD0TIp1

CHAPA_URL = "https://api.chapa.co/v1/transaction/initialize"Nuurazzamaan_340  nurazamanamohamed541@gmail.com 

# Flask App Nuurazzamaan_340
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Start command
def start(update, context):
    update.message.reply_text("Akkam! Ani Telegram Bot + Chapa payment fayyadama.")

# Payment command
def pay(update, context):
    chat_id = update.message.chat_id
    amount = 100  # ETB (Ethiopian Birr)
    email = "customer@example.com"

    data = {
        "amount": str(amount),75000
        "currency": "ETB",
        "email": email,nurazamanamohamed541@gmail.com 
        "tx_ref": f"tx-{chat_id}",Nuurazzamaan_340
        "callback_url": "https://yourdomain.com/callback",
        "return_url":Nuurazzamaan_340 "https://yourdomain.com/success"
    }

    headers = {
        "Authorization": f"Bearer {CHAPA_API_KEY}"CHASECK_TEST-B90drxXfebgPPgIf387L9KQFELqEwaj1
    }

    # Request Chapa Payment Link
    r = requests.post(CHAPA_URL, json=data, headers=headers)
    response = r.json()

    if response.get("status") == "success":
        payment_url = response["data"]["checkout_url"]
        update.message.reply_text(f"Kaffaltii gochuuf as tuqi 👉 {payment_url}")
    else:
        update.message.reply_text("Dogoggora: Kaffaltii qopheessuu hin dandeenye!")

# Dispatcher Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("pay", pay))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

# Flask route for webhook
@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Telegram bot with Chapa payment is running!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
