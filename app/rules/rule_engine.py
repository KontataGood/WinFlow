"""
==========================================================
Rule Engine
==========================================================

Назначение
----------
RuleEngine отвечает за обработку событий и поиск правил,
которые должны быть применены к этим событиям.

Общая схема:

    EventBus
       │
       ▼
    RuleEngine
       │
       ▼
    RuleManager
       │
       ▼
    Rule
       │
       ▼
    Conditions

RuleEngine не выполняет действия самостоятельно.

После определения подходящего правила его action
будет передан в отдельную систему выполнения действий.

Проект:
    Autom Task
"""

from app.core.event import Event
from app.rules.rule_manager import RuleManager
from app.actions.action_dispatcher import ActionDispatcher
from app.conditions.condition_checker import ConditionChecker


class RuleEngine:
    """
    Движок обработки правил Autom Task.

    Получает события из EventBus и проверяет,
    какие правила соответствуют этим событиям.
    """

    def __init__(
        self,
        event_bus,
        rule_manager: RuleManager
    ):
        """
        Инициализация RuleEngine.

        Args:
            event_bus:
                Шина событий приложения.

            rule_manager:
                Менеджер правил.
        """

        self._event_bus = event_bus
        self._rule_manager = rule_manager
        self._action_dispatcher = ActionDispatcher()

        self._register_handlers()

        self._condition_checker = ConditionChecker()

    def _register_handlers(self):
        """
        Регистрирует обработчик событий.

        RuleEngine должен получать все события,
        чтобы самостоятельно определить,
        какие правила подходят.
        """

        self._event_bus.subscribe_all(
            self._handle_event
        )

    def _handle_event(self, event: Event):
        """
        Обрабатывает полученное событие.

        На данном этапе метод только ищет
        подходящие правила.

        Выполнение действий будет добавлено позже.
        """

        rules = self._rule_manager.get_enabled_rules()

        for rule in rules:

            if rule.event_type != event.type:
                continue

            if not self._condition_checker.check(
                rule.conditions,
                event.data
            ):
                continue

            print(
                f"Rule matched: {rule.name}"
            )

            for action in rule.actions:
                self._action_dispatcher.execute(
                    action
                )