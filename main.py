import logging
import sys

from config import bot, dp
import asyncio
from handlers.recipes import recipe_router
from handlers.start import start_router
from handlers.my_info import myinfo_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router


async def main() -> None:
    dp.include_router(start_router)
    dp.include_router(recipe_router)
    dp.include_router(myinfo_router)
    dp.include_router(dishes_router)
    dp.include_router(review_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
