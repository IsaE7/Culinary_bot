from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command

myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Your id: {user_id}\nYour name: {first_name}\nYour nickname: {username}")