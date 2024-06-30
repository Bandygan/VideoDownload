import asyncio
from telegram import Bot

# Ваш токен бота, полученный от BotFather
TOKEN = '7234654837:AAF_J6GRNPS9EMguhUYFtKXhyjV1FLsCOuI'

# Создайте экземпляр бота
bot = Bot(token=TOKEN)

# ID чата пользователя (замените на реальный chat_id)
chat_id = '520969390'

# Сообщение, которое вы хотите отправить
message = 'Скоро я буду воровать видео из интернета, и мне ничего за это не сделают.'

async def send_message():
    await bot.send_message(chat_id=chat_id, text=message)

# Запустите асинхронную функцию
asyncio.run(send_message())



