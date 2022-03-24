from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    contact = State()
    add_coworker = State()
    coworkers_state = State()
    politeness = State()
    speed = State()
    knowledge = State()
    purity = State()
    comment = State()
    del_teacher = State()