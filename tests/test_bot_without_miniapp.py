import unittest

from bot.cases import format_case_details, get_case_by_button
from bot.keyboards import main_menu


class BotWithoutMiniAppTests(unittest.TestCase):
    def test_main_menu_uses_plain_telegram_buttons(self) -> None:
        keyboard = main_menu()
        buttons = [button for row in keyboard.keyboard for button in row]

        self.assertGreaterEqual(len(buttons), 4)
        self.assertTrue(all(button.web_app is None for button in buttons))
        self.assertIn("Beauty: запись в салон", [button.text for button in buttons])
        self.assertIn("Shop: магазин", [button.text for button in buttons])
        self.assertIn("AI Survey: опросник", [button.text for button in buttons])
        self.assertIn("Admin: дашборд", [button.text for button in buttons])

    def test_case_catalog_resolves_reply_button_text(self) -> None:
        demo_case = get_case_by_button("Shop: магазин")

        self.assertIsNotNone(demo_case)
        self.assertEqual(demo_case.slug, "ecommerce_shop")
        self.assertIn("витрина", format_case_details(demo_case).lower())

    def test_unknown_reply_button_returns_none(self) -> None:
        self.assertIsNone(get_case_by_button("Unknown"))


if __name__ == "__main__":
    unittest.main()
