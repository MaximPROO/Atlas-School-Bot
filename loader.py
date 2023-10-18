from aiogram import Dispatcher, Bot
from data.config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot, storage=storage)


