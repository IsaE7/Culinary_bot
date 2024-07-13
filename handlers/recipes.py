from aiogram.types import FSInputFile

from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
import random

recipe_router = Router()

# recipes = [
#     "Рецепт 1: Салат 'Цезарь'",
#     "Рецепт 2: Борщ",
#     "Рецепт 3: Паста 'Карбонара'",
#     "Рецепт 4: Плов",
#     "Рецепт 5: Блинчики"
#
# ]

recipe = {
    'ice_cola': 'images/ice_kola.jpg',
    'blinchiki': 'images/blinchiki.jpg',
    'Plov': 'images/plov.jpg',
    'Borsch': 'images/borsch.jpg',
}


@recipe_router.message(Command('random_recipe'))
async def send_random_recipe(message: types.Message):
    random_recipe_name = random.choice(list(recipe.keys()))
    # recipe = random.choice(recipes)
    # await message.reply(recipe)
    photo = FSInputFile(recipe[random_recipe_name])
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption=random_recipe_name
    )