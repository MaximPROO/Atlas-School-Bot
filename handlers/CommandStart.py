from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from loader import dp
from aiogram.types import Message
from keyboards.keyboards import menu_keyb
from utils.db import add_user, session, User


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    existing_user = session.query(User).filter(User.tg_id == message.from_user.id).first()
    if existing_user:
        await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n"
                             f"Sizni yana bir bora ko'rib turganimdan xursandman", reply_markup=menu_keyb)
    else:

        await add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
        print(f"|INFO| User {message.from_user.full_name} added!")
        await message.reply(f"Assalomu alaykum {message.from_user.full_name}!\n"
                            f"Atlas School botga xush kelibsiz!\n", reply_markup=menu_keyb)


@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    await message.reply(f"Assalomu alaykum {message.from_user.full_name}!\n")
