import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import F
from state import Form
from lyrics import extract_lyrics
from aiogram.fsm.context import FSMContext

TOKEN = "YOUR TOKEN HERE"
dp = Dispatcher()

@dp.message(CommandStart())
async def starting(message: Message):
    await message.answer(text="Assalomu alaykum, bu bot orqali siz qo'shiqni tekstga aylantirishingiz mumkin!\n/findsong deb yozing!")
    
@dp.message(Command('findsong'))
async def artist_yuborish(message: Message, state: FSMContext):
    
    await state.set_state(Form.artist)
    await message.answer(text="Qo'shiqchining ismini kiriting!")
    
@dp.message(F.text, Form.artist)
async def artist_olish(message: Message, state: FSMContext):
    
    await state.update_data(artist=message.text)
    await state.set_state(Form.song)
    
    await message.answer(text="Qo'shiqning nomini kiriting!")
    
@dp.message(F.text, Form.song)
async def song_olish(message: Message, state: FSMContext):
    
    await state.update_data(song=message.text)
    
    data = await state.get_data()
    artist = str(data.get('artist'))
    song = str(data.get('song'))
    
    extract_lyrics(artist=artist, song=song)
    
    doc = FSInputFile(f"{artist}-{song.lower()}.txt")
    
    await message.answer_document(document=doc)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())