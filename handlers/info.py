from loader import dp
from aiogram.types import Message
from keyboards.keyboards import courses_kb, it_courses


@dp.message_handler(text="Biz Haqimida 🔹")
async def cmd_info(message: Message):
    await message.reply(f"Number One School o'quv markazi.\n"
                        f"Mazil: Samarqand shaharAbu Rayhon Beruniy ko'chasi, 67\n"
                        f"Orintir: Eski bilayn, KIWI market\n"
                        f"Bizning telefon raqamlar +998 (99) 597 19 94\n"
                        f"Office raqam +998 (90)  602 77 03")


# send courses

@dp.message_handler(text="Barcha Kurslar 🔹")
async def cmd_redirect_courses(message: Message):
    await message.answer("Bizda mavjud kurslar", reply_markup=courses_kb)


@dp.message_handler(text="IT Kurslar 🔹")
async def cmd_redirect_courses(message: Message):
    await message.answer("Bizda mavjud IT kurslar", reply_markup=it_courses)