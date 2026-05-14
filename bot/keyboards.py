from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from shared.config import Settings


def main_menu(settings: Settings) -> InlineKeyboardMarkup:
    base_url = settings.webapp_base_url
    version = "v=3"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Beauty: запись в салон",
                    web_app=WebAppInfo(url=f"{base_url}/beauty_booking/index.html?{version}"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Shop: магазин",
                    web_app=WebAppInfo(url=f"{base_url}/ecommerce_shop/index.html?{version}"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="AI Survey: опросник",
                    web_app=WebAppInfo(url=f"{base_url}/ai_survey/index.html?{version}"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Admin: дашборд",
                    web_app=WebAppInfo(url=f"{base_url}/admin_panel/index.html?{version}"),
                )
            ],
        ]
    )
