from telegram.ext import Updater, CommandHandler

# ======== جایگزین کن با توکن خودت ========
TOKEN = "8478052154:AAF_lpW7or9m_QVpz2CdRgCL8qQv_yff6So"

# تابع پاسخ به /start
def start(update, context):
    update.message.reply_text("سلام! ربات با موفقیت روشن شد ✅")

# ساخت updater و dispatcher
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# اضافه کردن دستور /start
dp.add_handler(CommandHandler("start", start))

# اجرای ربات
print("ربات روشن شد... ✅")
updater.start_polling()
updater.idle()
