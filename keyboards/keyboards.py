from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

courses_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Prezident maktabiga tayorlash 👩‍🎓")
        ],
        [
            KeyboardButton(text="Matematika 🔹"),
            KeyboardButton(text="English 🔹"),
        ],
        [
            KeyboardButton(text="Logic 🔹"),
            KeyboardButton(text="Tandiqiy fikrlash 🔹"),
        ],
        [
            KeyboardButton(text="Mental Arifmetika 🔹"),
            KeyboardButton(text="ILEST 🔹"),
            KeyboardButton(text="Russia Language 🇷🇺"),
        ],
        [
            KeyboardButton("Kompyuter Savodxonligi 🔹"),
            KeyboardButton("Frontend dasturlash 🔹"),
        ],
        [
            KeyboardButton("Backend dasturlash 🔹"),
            KeyboardButton(text="Graphic design 🔹"),
        ]
    ], resize_keyboard=True
)

menu_keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Barcha Kurslar 🔹"),
            KeyboardButton(text="Biz Haqimida 🔹"),
        ],
        [
            KeyboardButton(text="Bizning manzil 🔹"),
            KeyboardButton(text="Bog'lanish 🔹"),
        ],
        [
            KeyboardButton(text="IT Kurslar 🔹"),
        ]
    ], resize_keyboard=True
)

days_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dushanba Chorshanba Juma", callback_data="d4j"),
        ],
        [
            InlineKeyboardButton(text="Seshanba Payshanba Shanba", callback_data="sps"),
        ]
    ]
)

times_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="08:00 -> 10:00", callback_data="08:00->10:00"),
            InlineKeyboardButton(text="10:00 -> 12:00", callback_data="10:00->12:00"),
        ],
        [
            InlineKeyboardButton(text="12:00 -> 14:00", callback_data="12:00->14:00"),
            InlineKeyboardButton(text="14:00 -> 16:00", callback_data="14:00->16:00"),
        ],
        [
            InlineKeyboardButton(text="16:00 -> 18:00", callback_data="16:00->18:00"),
            InlineKeyboardButton(text="18:00 -> 20:00", callback_data="18:00->20:00"),
        ]
    ]
)

y_n_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha ✅", callback_data="yes"),
            InlineKeyboardButton(text="Yo'q ❌", callback_data="no"),
        ]
    ]
)

it_courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend dasturlash 🔹"),
            KeyboardButton(text="Backend dasturlash 🔹"),
        ],
        [
            KeyboardButton(text="Graphic design 🔹"),
            KeyboardButton(text="Kompyuter Savodxonligi 🔹"),
        ],
        [
            KeyboardButton(text="SMM marketing 🔹"),
            KeyboardButton(text="Axborot xavfsizligi 🔹"),
        ]
    ], resize_keyboard=True
)