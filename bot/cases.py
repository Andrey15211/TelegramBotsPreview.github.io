from dataclasses import dataclass


@dataclass(frozen=True)
class DemoCase:
    slug: str
    button_text: str
    title: str
    summary: str
    features: tuple[str, ...]
    next_action: str


DEMO_CASES: tuple[DemoCase, ...] = (
    DemoCase(
        slug="beauty_booking",
        button_text="Beauty: запись в салон",
        title="Beauty: запись в салон",
        summary="Бот помогает выбрать услугу, мастера и удобное время без Mini App.",
        features=(
            "каталог услуг и цен",
            "быстрая заявка на запись",
            "подтверждение заявки в чате",
        ),
        next_action="Напишите: Хочу записаться на услугу, дата и время.",
    ),
    DemoCase(
        slug="ecommerce_shop",
        button_text="Shop: магазин",
        title="Shop: магазин",
        summary="Чатовая витрина товаров с подбором, корзиной и заявкой на заказ.",
        features=(
            "витрина популярных товаров",
            "подбор по запросу клиента",
            "оформление заказа через сообщение",
        ),
        next_action="Напишите товар, количество и контакт для связи.",
    ),
    DemoCase(
        slug="ai_survey",
        button_text="AI Survey: опросник",
        title="AI Survey: опросник",
        summary="Опросник собирает ответы в диалоге и помогает квалифицировать заявку.",
        features=(
            "пошаговые вопросы",
            "сбор предпочтений клиента",
            "итоговая заявка для менеджера",
        ),
        next_action="Напишите: Начать опрос.",
    ),
    DemoCase(
        slug="admin_panel",
        button_text="Admin: дашборд",
        title="Admin: дашборд",
        summary="Админ-сценарий показывает, какие команды можно вынести в Telegram.",
        features=(
            "просмотр новых заявок",
            "смена статусов",
            "быстрые уведомления администратору",
        ),
        next_action="Напишите: Покажи заявки.",
    ),
)


def get_case_by_button(text: str) -> DemoCase | None:
    normalized = text.strip()
    return next((demo_case for demo_case in DEMO_CASES if demo_case.button_text == normalized), None)


def format_case_details(demo_case: DemoCase) -> str:
    features = "\n".join(f"- {feature}" for feature in demo_case.features)
    return (
        f"{demo_case.title}\n\n"
        f"{demo_case.summary}\n\n"
        f"Что умеет:\n{features}\n\n"
        f"Следующий шаг: {demo_case.next_action}"
    )
