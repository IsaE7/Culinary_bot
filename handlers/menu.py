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


CATEGORIES = ("Breakfasts", "Soups", "Basic", "Beverage")


@menu_router.message(F.text.in_(CATEGORIES))
async def breakfasts_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT dishes.*, categories.name FROM dishes 
        JOIN categories ON categories.id=dishes.categories_id
        WHERE LOWER(categories.name) = ?
    """
    categories = message.text.lower()
    print("Categories: ", categories)

    try:
        print("Executing query with params:", (categories,))
        dishes = database.fetch(
            query=sqlquery,
            params=(categories,)
        )
    except Exception as e:
        await message.answer("An error occurred while fetching data from the database.")
        print(f"Database error: {e}")
        return

    print("Query result:", dishes)
    if not dishes:
        await message.answer("Unfortunately, there are no dishes in this category.")
        return

    await message.answer(f"Dish category {categories}", reply_markup=kb)
    for dish in dishes:
        try:
            caption = f"Name: {dish.get('name')}\nPrice: {dish.get('price')}"
            if dish.get('cover'):
                photo = FSInputFile(dish.get('cover'))
                await message.answer_photo(photo=photo, caption=caption)
            else:
                await message.answer(caption)
        except Exception as e:
            await message.answer(f"An error occurred while sending dish information.")
            print(f"Error sending dish info: {e}")

# @menu_router.message(F.text.in_(CATEGORIES))
# async def breakfasts_handler(message: types.Message):
#     kb = types.ReplyKeyboardRemove()
#     sqlquery = """
#         SELECT dishes.*, categories.name FROM dishes
#         JOIN categories ON categories.id=dishes.categories_id
#         WHERE categories.name = ?
#     """
#     categories = message.text.lower()
#     print("Categories: ", categories)
#     dishes = database.fetch(
#         query=sqlquery,
#         params=(categories,)
#     )
#     print(dishes)
#     if not dishes:
#         await message.answer("Unfortunately, there are no dishes in this category.")
#
#     await message.answer(f"Dish category{categories}", reply_markup=kb)
#     for dish in dishes:
#         photo = FSInputFile(dish.get('cover'))
#         await message.answer_photo(
#             caption=f"Name: {dish.get('name')}\nPrice: {dish.get('price')}",
#             photo=photo
#         )

