# Telegram Demo Bots

Модульная демо-структура для 4 чатовых Telegram-сценариев на `aiogram 3.x`.
Mini App/WebApp-интеграция отключена: бот работает обычными сообщениями и reply-кнопками.

## Запуск

1. Установите зависимости:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Создайте `.env` по примеру `.env.example` и укажите `API_TOKEN`.

3. Запустите бота:

```powershell
python -m bot.main
```

## Команды

- `/start` - открыть главное меню
- `/menu` - показать сценарии
- `/links` - сообщает, что Mini App-ссылки отключены
