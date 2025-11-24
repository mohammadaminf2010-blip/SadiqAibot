from telegram.ext import Updater, CommandHandler
import os

TOKEN = "8478052154:AAEFoZ2s5RXuX2BWLmP38OUV0CsggUQ6Qow"

def start(update, context):
    update.message.reply_text("ربات فعاله ✔")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
