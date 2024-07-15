import logging
import sys

from config import bot, dp , database
import asyncio
from handlers.recipes import recipe_router
from handlers.start import start_router
from handlers.my_info import myinfo_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router
from aiogram import Bot


async def on_startup(bot: Bot):
    database.create_tables()


async def main() -> None:
    dp.include_router(start_router)

    dp.include_router(recipe_router)
    dp.include_router(myinfo_router)
    dp.include_router(dishes_router)

    dp.include_router(review_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
