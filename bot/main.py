import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers.menu import router as menu_router
from shared.config import get_settings
from shared.database import init_db


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    await init_db()

    bot = Bot(token=settings.api_token)
    dispatcher = Dispatcher()
    dispatcher.include_router(menu_router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
