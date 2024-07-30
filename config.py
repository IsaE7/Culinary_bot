from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
from database.database import Database


load_dotenv()
database = Database("db.sqlite3")
debug = getenv("DEBUG", 0)
if not debug:
    print("The bot runs on the server")
    from aiogram.client.session.base import AiohttpSession
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("TOKEN"), session=session)
else:
    print("The bot is running on the computer")
    bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()
