from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command

unique_users = set()

start_router = Router()


@start_router.message(Command('start'))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if user_id not in unique_users:
        unique_users.add(user_id)
    await message.reply(f"Hello, {first_name}! Our bot already serves {len(unique_users)} unique users.")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Our website", url="https://vk.com/showtime7isa"),
            ],
            [
                types.InlineKeyboardButton(text="Our Instagram", url="https://www.instagram.com/djisae7?igsh=bTV5MXBmNGVrYmZj&utm_source=qr"),
            ],
            [
                types.InlineKeyboardButton(text="About Us", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="Review", callback_data="review"),
            ],
            [
                types.InlineKeyboardButton(text='Jobs', callback_data="jobs"),
            ],
            [
                types.InlineKeyboardButton(text="leave feedback", callback_data="feedback"),
            ]
        ]
    )
    await message.answer('Welcome', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us(call: types.CallbackQuery):
    await call.answer('Hello! Our culinary bot is your reliable kitchen assistant.')


@start_router.callback_query(F.data == 'review')
async def review(call: types.CallbackQuery):
    await call.answer('nothing yet')


@start_router.callback_query(F.data == 'jobs')
async def jobs(call: types.CallbackQuery):
    await call.answer('coming soon')
