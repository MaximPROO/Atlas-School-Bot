from data.config import ADMINS
from loader import dp


async def notify_admins():
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot started")
        except:
            pass
