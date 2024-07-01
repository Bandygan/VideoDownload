import os
from datetime import datetime, timedelta

# Установите переменную окружения DJANGO_SETTINGS_MODULE перед настройкой Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jwt_project.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from django.conf import settings
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from youtubesearchpython import Video, ResultMode
from pytube import YouTube
from jwt_project.models import UserProfile

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"got start command. code: {context.args}")
    answer = "Successfully connected."
    try:
        keyword = context.args.pop()
        profile = UserProfile.objects.get(telegram_setup_code=keyword)
        profile.telegram_id = update.effective_user.id
        profile.save()
    except Exception as e:
        answer = f"Something went wrong. Please try again later. {e}"
    await update.message.reply_text(answer)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.download(dirname())
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=filename,
        )
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invalid URL or an error occurred: {e}")

def dirname():
    dirname_ = datetime.today().strftime('%Y-%m-%d')
    if not os.path.isdir(dirname_):
        os.mkdir(dirname_)
    try:
        os.rmdir((datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d'))
    except Exception as e:
        print(f"Error removing old directory: {e}")
    return dirname_

app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
app.add_handler(CommandHandler("start", start))
app.add_handler(echo_handler)
app.run_polling()
