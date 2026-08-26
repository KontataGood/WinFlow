"""
==========================================================
Rule
==========================================================

Модель правила автоматизации WinFlow.

Rule описывает условие, при котором должно
быть выполнено определенное действие.

Общая структура:

    Event
       │
       ▼
    Rule
       │
       ├── Conditions
       │
       └── Action

Rule не выполняет действие самостоятельно.
Она только хранит описание правила.

Выполнением правил будет заниматься RuleEngine.

Проект:
    WinFlow
"""


class Rule:
    """
    Описывает одно правило автоматизации WinFlow.
    """

    def __init__(
        self,
        name: str,
        event_type,
        conditions: dict,
        actions: list[dict],
        enabled: bool = True
    ):
        """
        Создает правило.

        Args:
            name:
                Уникальное или понятное пользователю
                название правила.

            event_type:
                Тип события, которое запускает правило.

            conditions:
                Набор условий, которые должны быть выполнены.

            action:
                Описание действия, которое необходимо выполнить.

            enabled:
                Включено ли правило.
        """

        self.name = name
        self.event_type = event_type
        self.conditions = conditions
        self.actions = actions
        self.enabled = enabled