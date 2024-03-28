from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    artist = State()
    song = State()
