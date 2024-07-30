from aiogram.enums import ChatMemberStatus

from config import group

from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import Bot, bot, database
from datetime import timedelta
from profanity_check import predict_prob
from config import group

group_router = Router()

BAD_WORDS = ("тупой", "дурак", "дебил")


@group_router.message(Command('ban', prefix="!"))
async def ban_user(message: types.Message):
    print(message.text)
    reply = message.reply_to_message
    print("Reply or not", reply)
    if reply:
        author = reply.from_user.id
        chat_id = message.chat.id
        bot_member = await bot.get_chat_member(chat_id, bot.id)
        if bot_member.status != ChatMemberStatus.ADMINISTRATOR:
            await message.reply("I need to be an administrator to ban users.")
            return

        await bot.ban_chat_member(
            chat_id=chat_id,
            user_id=author,
            until_date=timedelta(seconds=60)
        )


def check_user_warnings(user_id: int, chat_id: int) -> int:
    user_warnings = database.fetch(
        query="""SELECT * FROM user_warnings WHERE user_id=? AND chat_id=?""",
        params=(user_id, chat_id),
        fetchmany=False
    )
    print(user_warnings)
    if not user_warnings:
        database.execute(
            query="""INSERT INTO user_warnings(user_id, chat_id, counter)
            VALUES (?, ?, 1)""",
            params=(user_id, chat_id)
        )
        return 1
    elif user_warnings.get('counter') < 5:
        database.execute(
            query="""UPDATE user_warnings
                     SET counter = counter + 1
                     WHERE user_id=? AND chat_id=?""",
            params=(user_id, chat_id)
        )
        return user_warnings.get('counter') + 1
    else:
        return 5


@group_router.message()
async def filter_bad_words(message: types.Message):
    is_bad_word = any(word in message.text.lower() for word in BAD_WORDS)

    badness = predict_prob([message.text])[0] >= 0.6

    if is_bad_word or badness:
        warnings = check_user_warnings(message.from_user.id, message.chat.id)

        if warnings >= 5:
            bot_member = await bot.get_chat_member(message.chat.id, bot.id)
            if bot_member.status != ChatMemberStatus.ADMINISTRATOR:
                await message.reply("I need to be an administrator to ban users.")
                return

            await bot.ban_chat_member(
                user_id=message.from_user.id,
                chat_id=message.chat.id,
                until_date=timedelta(seconds=60)
            )

        if is_bad_word:
            try:
                await message.delete()
                await message.answer(
                    f'Do not use offensive language {message.from_user.first_name}'
                )
            except Exception as e:
                print(f"Error: {e}")

        if badness:
            try:
                await message.delete()
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'User: {message.from_user.first_name}, you have written a bad word!!!'
                )
            except Exception as e:
                print(f"Error: {e}")
