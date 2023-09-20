from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = -1001942761552
ADMIN_ID1 = 761771256
BOT_GIF = r"C:\Users\NOTNIK_KG\Desktop\pythonProject\media\joinblink-blink.gif"
DESTINATION_DIR = r"C:\Users\NOTNIK_KG\Desktop\pythonProject\media"