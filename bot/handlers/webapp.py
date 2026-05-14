import json
from typing import Any

from aiogram import Router
from aiogram.types import Message

from shared.database import SessionLocal
from shared.orders import create_order


router = Router()


def parse_price(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


@router.message(lambda message: message.web_app_data is not None)
async def web_app_data(message: Message) -> None:
    raw_data = message.web_app_data.data if message.web_app_data else "{}"

    try:
        payload = json.loads(raw_data)
    except json.JSONDecodeError:
        await message.answer("Не удалось прочитать данные WebApp.")
        return

    service_name = str(payload.get("service_name") or payload.get("case") or "WebApp order")
    price = parse_price(payload.get("price") or payload.get("total"))
    status = str(payload.get("status") or "new")
    user_id = message.from_user.id if message.from_user else 0

    async with SessionLocal() as session:
        order = await create_order(
            session,
            user_id=user_id,
            service_name=service_name,
            price=price,
            status=status,
        )

    await message.answer(
        "Данные из WebApp получены.\n"
        f"Заказ #{order.id}\n"
        f"Услуга: {order.service_name}\n"
        f"Стоимость: {order.price} ₽\n"
        f"Статус: {order.status}"
    )
