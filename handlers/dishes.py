from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile

dishes_router = Router()


@dishes_router.message(F.text == 'Beverages')
async def drinks(message: types.Message):
    photo = FSInputFile('images/ice_kola.jpg')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='ice_kola'
    )


@dishes_router.message(F.text == 'Dish')
async def foods(message: types.Message):
    photo = FSInputFile('images/blinchiki.jpg')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='blinchik'
    )
