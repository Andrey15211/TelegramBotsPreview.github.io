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
    await message.answer(
        f"Демо-кейсы на Vercel:\n{settings.webapp_base_url}",
        reply_markup=main_menu(settings),
    )


@router.message(Command("webapp_url"))
async def webapp_url(message: Message) -> None:
    settings = get_settings()
    await message.answer(f"WEBAPP_BASE_URL: {settings.webapp_base_url}")


@router.message(Command("links"))
async def links(message: Message) -> None:
    settings = get_settings()
    base_url = settings.webapp_base_url
    version = "v=3"
    await message.answer(
        "Текущие WebApp-ссылки:\n"
        f"Beauty: {base_url}/beauty_booking/index.html?{version}\n"
        f"Shop: {base_url}/ecommerce_shop/index.html?{version}\n"
        f"Survey: {base_url}/ai_survey/index.html?{version}\n"
        f"Admin: {base_url}/admin_panel/index.html?{version}"
    )
