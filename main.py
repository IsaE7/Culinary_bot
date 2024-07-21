import logging
import sys

from config import bot, dp, database
import asyncio

from aiogram import Bot
from handlers import (
    private_router,
    group_router
)


async def on_startup(bot: Bot):
    database.create_tables()


async def main() -> None:
    dp.include_router(private_router)
    dp.include_router(group_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
