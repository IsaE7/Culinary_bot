from aiogram import Router, F

from .dishes import dishes_router
from .menu import menu_router
from .my_info import myinfo_router
from .recipes import recipe_router
from .review_dialog import review_router
from .start import start_router
from .group import group_router
from .house_kg import house_router


private_router = Router()
private_router.include_router(start_router)
private_router.include_router(dishes_router)
private_router.include_router(menu_router)
private_router.include_router(myinfo_router)
private_router.include_router(recipe_router)
private_router.include_router(house_router)
private_router.include_router(review_router)

private_router.message.filter(F.chat.type == 'private')
