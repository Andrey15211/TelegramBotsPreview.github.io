# Telegram WebApps Demo Bots

Модульная демо-структура для 4 кейсов Telegram WebApps на `aiogram 3.x`.

## Запуск

1. Установите зависимости:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Создайте `.env` по примеру `.env.example` и укажите `API_TOKEN`.

Для кнопок Telegram WebApp используйте только HTTPS:

```powershell
WEBAPP_BASE_URL=https://telegram-bots-preview-github-io.vercel.app/webapps
```

`http://127.0.0.1:8000/webapps` подходит только для теста страниц в браузере. Telegram отклонит такой URL в inline-кнопке.

3. Поднимите локальный сервер для WebApps:

```powershell
python -m http.server 8000
```

4. В другом терминале запустите бота:

```powershell
python -m bot.main
```

Локальные WebApp URL для браузерного теста:

- Beauty: `http://127.0.0.1:8000/webapps/beauty_booking/index.html`
- Shop: `http://127.0.0.1:8000/webapps/ecommerce_shop/index.html`
- AI Survey: `http://127.0.0.1:8000/webapps/ai_survey/index.html`
- Admin: `http://127.0.0.1:8000/webapps/admin_panel/index.html`

Для открытия WebApp внутри Telegram обычно нужен публичный HTTPS URL. Для локальной разработки используйте туннель вроде ngrok/cloudflared и замените `WEBAPP_BASE_URL`.
