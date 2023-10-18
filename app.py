from loader import dp
import handlers
from aiogram import executor


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


