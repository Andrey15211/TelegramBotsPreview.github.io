from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.cases import format_case_details, get_case_by_button
from bot.keyboards import main_menu


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Выберите демонстрационный сценарий:",
        reply_markup=main_menu(),
    )


@router.message(Command("menu"))
async def menu(message: Message) -> None:
    await message.answer(
        "Выберите кейс в меню ниже. Все сценарии работают прямо в Telegram-чате.",
        reply_markup=main_menu(),
    )


@router.message(Command("links"))
async def links(message: Message) -> None:
    await message.answer(
        "Mini App-ссылки отключены. Используйте кнопки меню, чтобы открыть чатовые сценарии."
    )


@router.message()
async def case_details(message: Message) -> None:
    if not message.text:
        return

    demo_case = get_case_by_button(message.text)
    if demo_case is None:
        await message.answer(
            "Не понял запрос. Нажмите /menu и выберите один из сценариев.",
        )
        return

    await message.answer(format_case_details(demo_case))
