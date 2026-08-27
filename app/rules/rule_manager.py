"""
==========================================================
Rule Manager
==========================================================

Назначение
----------
Управление правилами автоматизации Autom Task.

RuleManager отвечает за загрузку правил из конфигурации
и создание объектов Rule.

RuleManager НЕ выполняет правила.

За выполнение правил будет отвечать RuleEngine.

Проект:
    Autom Task
"""

from app.rules.rule import Rule
from app.platforms.platform_resolver import PlatformResolver
from app.core.event_type import EventType
from app.conditions.condition import Condition
from app.conditions.condition_operator import ConditionOperator
from app.rules.rule_validator import (
    RuleValidator,
    RuleValidationError
)


class RuleManager:
    """
    Управляет набором правил Autom Task.
    """

    def __init__(self, configuration):
        """
        Инициализация RuleManager.

        Args:
            configuration:
                Экземпляр ConfigManager.
        """

        self._configuration = configuration

        self._validator = RuleValidator()

        self._platform_resolver = PlatformResolver()

        self._rules = []

        self._load_rules()


    def _load_rules(self):
        """
        Загружает правила из конфигурации.

        Некорректные правила пропускаются,
        остальные продолжают загружаться.
        """

        rules = self._configuration.get(
            "rules",
            []
        )

        for rule_data in rules:

            try:
                # Проверяем структуру правила
                self._validator.validate(rule_data)

                # Создаём условия
                conditions = []

                for condition_data in rule_data.get(
                    "conditions",
                    []
                ):
                    operator = ConditionOperator(
                        condition_data["operator"]
                    )

                    conditions.append(
                        Condition(
                            field=condition_data["field"],
                            operator=operator,
                            value=self._platform_resolver.resolve(
                                condition_data["value"]
                            )
                        )
                    )

                # Тип события
                event_type = EventType[
                    rule_data["event"]
                ]

                # Создаём правило
                rule = Rule(
                    name=rule_data["name"],
                    event_type=event_type,
                    conditions=conditions,
                    actions=rule_data.get(
                        "actions",
                        []
                    ),
                    enabled=rule_data.get(
                        "enabled",
                        True
                    )
                )

                self._rules.append(rule)

            except (RuleValidationError, ValueError, KeyError) as error:
                print(
                    f"Invalid rule "
                    f"'{rule_data.get('name', '<unknown>')}': "
                    f"{error}"
                )

    def get_rules(self):
        """
        Возвращает все загруженные правила.
        """

        return self._rules

    def get_enabled_rules(self):
        """
        Возвращает только включенные правила.
        """

        return [
            rule
            for rule in self._rules
            if rule.enabled
        ]