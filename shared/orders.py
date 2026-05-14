from sqlalchemy.ext.asyncio import AsyncSession

from shared.models import Order


async def create_order(
    session: AsyncSession,
    *,
    user_id: int,
    service_name: str,
    price: int,
    status: str = "new",
) -> Order:
    order = Order(user_id=user_id, service_name=service_name, price=price, status=status)
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order
