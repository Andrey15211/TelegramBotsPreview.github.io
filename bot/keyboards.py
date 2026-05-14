from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Beauty: запись в салон")],
            [KeyboardButton(text="Shop: магазин")],
            [KeyboardButton(text="AI Survey: опросник")],
            [KeyboardButton(text="Admin: дашборд")],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )
