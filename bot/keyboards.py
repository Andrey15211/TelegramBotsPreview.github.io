from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

from shared.config import Settings


def main_menu(settings: Settings) -> ReplyKeyboardMarkup:
    base_url = settings.webapp_base_url
    version = "v=3"

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Beauty: запись в салон",
                    web_app=WebAppInfo(url=f"{base_url}/beauty_booking/index.html?{version}"),
                )
            ],
            [
                KeyboardButton(
                    text="Shop: магазин",
                    web_app=WebAppInfo(url=f"{base_url}/ecommerce_shop/index.html?{version}"),
                )
            ],
            [
                KeyboardButton(
                    text="AI Survey: опросник",
                    web_app=WebAppInfo(url=f"{base_url}/ai_survey/index.html?{version}"),
                )
            ],
            [
                KeyboardButton(
                    text="Admin: дашборд",
                    web_app=WebAppInfo(url=f"{base_url}/admin_panel/index.html?{version}"),
                )
            ],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )
