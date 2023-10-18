from loader import dp
from aiogram import types

async def set_bot_command():
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand(command="/start", description="Start"),
            types.BotCommand(command="/help", description="Help"),
        ]
    )