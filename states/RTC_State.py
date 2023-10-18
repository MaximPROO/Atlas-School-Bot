from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterToCours(StatesGroup):
    choised_course = State()
    choised_day = State()
    choised_time = State()
    phone = State()
    result = State()