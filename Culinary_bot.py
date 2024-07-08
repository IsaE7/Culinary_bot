import asyncio
import logging
import os
import random
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

recipes = [
    "Рецепт 1: Салат 'Цезарь'",
    "Рецепт 2: Борщ",
    "Рецепт 3: Паста 'Карбонара'",
    "Рецепт 4: Плов",
    "Рецепт 5: Блинчики"
]

unique_users = set()


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if user_id not in unique_users:
        unique_users.add(user_id)
    await message.reply(f"Привет, {first_name}! Наш бот обслуживает уже {len(unique_users)} уникальных пользователей.")


@dp.message(Command('myinfo'))
async def send_myinfo(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}")


@dp.message(Command('random_recipe'))
async def send_random_recipe(message: types.Message):
    recipe = random.choice(recipes)
    await message.reply(recipe)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
