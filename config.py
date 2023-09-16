from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
ADMIN_ID = -1001942761552
ADMIN_ID1 = 761771256
BOT_GIF = r"C:\Users\NOTNIK_KG\Desktop\pythonProject\media\joinblink-blink.gif"
