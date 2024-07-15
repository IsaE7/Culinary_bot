from contourpy.util import data

from config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import database


class CulinaryReview(StatesGroup):
    name: State = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


review_router = Router()


user_reviews = {}


@review_router.callback_query(F.data == 'feedback')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    if user_id in user_reviews:
        await call.message.answer("You have already left a review.")
        await state.clear()
    else:
        await state.set_state(CulinaryReview.name)
        await call.message.answer("Your name: ")


@review_router.message(CulinaryReview.name)
async def process_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await message.answer("Your Instagram name: ")
        await state.set_state(CulinaryReview.instagram_username)
        await state.update_data(name=message.text)
        data = await state.get_data()
        print(data['name'])


@review_router.message(CulinaryReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await message.answer("Your visit date: ")
        await state.set_state(CulinaryReview.visit_date)
        await state.update_data(instagram_username=message.text)
        data = await state.get_data()
        print(data['instagram_username'])


@review_router.message(CulinaryReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await state.set_state(CulinaryReview.food_rating)
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text='bad', callback_data='5')],
                [types.KeyboardButton(text='good', callback_data='10')],
            ],
            resize_keyboard=True
        )
        await message.answer("Your food rating: ", reply_markup=kb)
        await state.update_data(visit_date=message.text)
        data = await state.get_data()
        print(data['visit_date'])


@review_router.message(CulinaryReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await state.set_state(CulinaryReview.cleanliness_rating)
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text='bad', callback_data='5')],
                [types.KeyboardButton(text='good', callback_data='10')],
            ],
            resize_keyboard=True
        )
        await message.answer("Your cleanliness rating: ", reply_markup=kb)
        await state.update_data(food_rating=message.text)
        data = await state.get_data()
        print(data['food_rating'])


@review_router.message(CulinaryReview.cleanliness_rating)
async def cleanliness_rating(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await state.set_state(CulinaryReview.extra_comments)
        kb = types.ReplyKeyboardRemove()
        await message.answer('Do you have any comments: ', reply_markup=kb)
        await state.update_data(cleanliness_rating=message.text)
        data = await state.get_data()
        print(data['cleanliness_rating'])


@review_router.message(CulinaryReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in user_reviews:
        await message.answer("You have already left a review.")
        await state.clear()
    else:
        await message.answer("Your review has been accepted.")
        user_reviews[user_id] = True
        await state.update_data(extra_comments=message.text)
        data = await state.get_data()
        print(data['extra_comments'])
        database.execute("""
            INSERT INTO survey_results(name, visit_date, instagram_name,
            food_rating, cleanliness_rating, extra_comments)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data['name'], data['20-06-2014'], data['IsaE7'], data['5'], data ['10'], data ['text']))
        await state.clear()
