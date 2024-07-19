from config import bot, dp, database
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
            ],
            # [
            #     types.InlineKeyboardButton(text="Menu", callback_data="categories"),
            # ]
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


# @start_router.callback_query(F.data == 'categories')
# async def categories(call: types.CallbackQuery):
#     categories_data = database.get_categories()
#     kb_data = []
#     for category in categories_data:
#         category_id = str(category[0])
#         category_name = str(category[1])
#         kb_data.append([types.InlineKeyboardButton(text=category_name, callback_data='category', category_id=category_id)])
#     kb = types.InlineKeyboardMarkup(inline_keyboard=kb_data)
#     await call.message.answer('chose one categories', reply_markup=kb)
#
#
# @start_router.callback_query(F.data == 'category')
# async def categories(call: types.CallbackQuery):
#     sqlquery = ("""
#             SELECT dishes.*, menu.name FROM dishes
#             JOIN menu ON menu.id=dishes.menu_id
#             WHERE menu.name = ?
#             """,
#     categories = ('Breakfasts', ))
#     """
#
#
#      d = call.data['category_id']
#     recipes = database.get_recipes_by_category()
#     for recipe in recipes:
#         recipe_name = str(recipe[0])
#         recipe_price = str(recipe[1])
#         recipe_cover = str(recipe[2])
#         await call.message.answer_photo(
#             photo=recipe_cover,
#             caption=f"recipe's name: {recipe_name}\nrecipe's price: {recipe_price}"
#         )


