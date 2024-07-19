from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from config import database

menu_router = Router()


@menu_router.message(Command("menu"))
async def menu_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Breakfasts")
            ],
            [
                types.KeyboardButton(text="Soups")
            ],
            [
                types.KeyboardButton(text="Basic")
            ],
            [
                types.KeyboardButton(text="Beverage")
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer(
        text="Select a food category",
        reply_markup=kb
    )


@menu_router.message(F.text == "Breakfasts")
async def breakfasts_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT dishes.*, categories.name FROM dishes 
        JOIN categories ON categories.id=dishes.categories_id
        WHERE categories.name = ?
    """
    categories = 'Breakfasts'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories,)
    )
    print(dishes)
    await message.answer("Dish category", reply_markup=kb)
    for dish in dishes:
        photo = FSInputFile(dish[3])
        await message.answer_photo(
            caption=f"Name: {dish[1]}\nPrice: {dish[2]}",
            photo=photo
        )


@menu_router.message(F.text == "Soups")
async def soups_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT dishes.*, categories.name FROM dishes 
        JOIN categories ON categories.id=dishes.categories_id
        WHERE categories.name = ?
    """
    categories = 'Soups'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories,)
    )
    print(dishes)
    await message.answer("Dish category", reply_markup=kb)
    for dish in dishes:
        photo = FSInputFile(dish[3])
        await message.answer_photo(
            caption=f"Name: {dish[1]}\nPrice: {dish[2]}",
            photo=photo
        )


@menu_router.message(F.text == "Basic")
async def basic_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT dishes.*, categories.name FROM dishes 
        JOIN categories ON categories.id=dishes.categories_id
        WHERE categories.name = ?
    """
    categories = 'Basic'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories,)
    )
    print(dishes)
    await message.answer("Dish category", reply_markup=kb)
    for dish in dishes:
        photo = FSInputFile(dish[3])
        await message.answer_photo(
            caption=f"Name: {dish[1]}\nPrice: {dish[2]}",
            photo=photo
        )


@menu_router.message(F.text == "Beverage")
async def beverage_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT dishes.*, categories.name FROM dishes 
        JOIN categories ON categories.id=dishes.categories_id
        WHERE categories.name = ?
    """
    categories = 'Beverage'

    dishes = database.fetch(
        query=sqlquery,
        params=(categories,)
    )
    print(dishes)
    await message.answer("Dish category", reply_markup=kb)
    for dish in dishes:
        photo = FSInputFile(dish[3])
        await message.answer_photo(
            caption=f"Name: {dish[1]}\nPrice: {dish[2]}",
            photo=photo
        )

