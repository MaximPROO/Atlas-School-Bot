from loader import dp
from aiogram.types import Message, CallbackQuery
from states.RTC_State import RegisterToCours as RTC
from keyboards.keyboards import y_n_kb, menu_keyb, days_kb, times_kb
from utils.db import record_user
from aiogram.dispatcher import FSMContext

var = [
    'Prezident maktabiga tayorlash 👩‍🎓', 'Matematika 🔹', 'Logic 🔹', 'Mental Arifmetika 🔹', 'ILEST 🔹',
    'Russia Language 🇷🇺', 'Tandiqiy fikrlash 🔹 ', 'English 🔹', 'Kompyuter Savodxonligi 🔹', 'Frontend dasturlash 🔹',
    'Backend dasturlash 🔹', 'Graphic design 🔹', 'Axborot xavfsizligi 🔹']


@dp.message_handler(text=var)
async def cmd_send(message: Message, state: FSMContext):
    await RTC.choised_course.set()
    choised_course = message.text.split()[0].lower()
    async with state.proxy() as data:
        data['choised_course'] = choised_course
    file = open(f'info_for_courses/{choised_course}.txt', 'r')
    msg = "\n".join(file.readlines())

    await message.answer(f"{msg}\nKursga yozilishni istaysizmi?", reply_markup=y_n_kb)
    await RTC.next()


@dp.callback_query_handler(state=RTC.choised_day, text=['yes', 'no'])
async def cmd_choised(call: CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await call.message.answer(f"Dars kunlarini tanlang", reply_markup=days_kb)
        await RTC.next()
    else:
        await state.finish()
        await call.message.answer("Bosh menu", reply_markup=menu_keyb)


@dp.callback_query_handler(state=RTC.choised_time, text=['d4j', 'sps'])
async def cmd_choised_time(call: CallbackQuery, state: FSMContext):
    if call.data == "dj4":
        async with state.proxy() as data:
            data['day'] = "dushanba chorshanba juma"
    else:
        async with state.proxy() as data:
            data['day'] = "seshanba payshanba shanba"

    await call.message.answer(f"Qaysi vaqt sizga qulay ?", reply_markup=times_kb)
    await RTC.next()


@dp.callback_query_handler(state=RTC.phone)
async def cmd_phone(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = call.data

    await call.message.answer(f"Bog'lanish uchun telefon raqamingizni kiriting")
    await RTC.next()


@dp.message_handler(state=RTC.result)
async def cmd_results(message: Message, state: FSMContext):

    phone = message.text
    uzb_operators = ['91', '90', '55', '50', '66', '94', '93', '88', '33', '77', '99', '98']
    if len(phone) == 13 and phone[0] == "+" and phone[1:4] == "998" and phone[4:6] in uzb_operators and phone != "+998999999999" and phone[1:].isnumeric():
        async with state.proxy() as data:
            data['phone'] = message.text
        await message.answer(f"Arizangiz qabul qilindi\n"
                             f"FIO: {message.from_user.first_name}\n"
                             f"Phone number {data['phone']}\n"
                             f"Tanlagan kuringiz {data['choised_course']}\n"
                             f"Tanlagan kun {data['day']}\n"
                             f"Tanlagan vaqt {data['time']}\n"
                             f"7 Ish kuni ichida sizga aloqaga chiqamiz! Raxmat")
        await record_user(
            name=message.from_user.full_name,
            tg_id=message.from_user.id,
            phone=data['phone'],
            choised_course=data['choised_course'],
            choised_day=data['day'],
            choised_time=data['time']
        )
        print(f"|INFO| User {message.from_user.full_name} added in cours {data['choised_course']}")
        await state.finish()
    else:
        await message.answer("Siz kiritgan raqam xato\nQaytadan urinib ko'ring\n"
                             "Namuna +998999999999")
