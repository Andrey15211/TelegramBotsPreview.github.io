from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.keyboards import main_menu
from shared.config import get_settings


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    settings = get_settings()
    await message.answer(
        "Выберите демонстрационный Telegram WebApp:",
        reply_markup=main_menu(settings),
    )


@router.message(Command("menu"))
async def menu(message: Message) -> None:
    settings = get_settings()
    await message.answer("Демо-кейсы:", reply_markup=main_menu(settings))
