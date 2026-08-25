"""
==========================================================
Rule Manager
==========================================================

Назначение
----------
Управление правилами автоматизации WinFlow.

RuleManager отвечает за загрузку правил из конфигурации
и создание объектов Rule.

RuleManager НЕ выполняет правила.

За выполнение правил будет отвечать RuleEngine.

Проект:
    WinFlow
"""

from app.rules.rule import Rule
from app.core.event_type import EventType


class RuleManager:
    """
    Управляет набором правил WinFlow.
    """

    def __init__(self, configuration):
        """
        Инициализация RuleManager.

        Args:
            configuration:
                Экземпляр ConfigManager.
        """

        self._configuration = configuration

        self._rules = []

        self._load_rules()

    def _load_rules(self):
        """
        Загружает правила из конфигурации.

        Если секция rules отсутствует,
        используется пустой список.
        """

        rules = self._configuration.get(
            "rules",
            []
        )

        for rule_data in rules:

            event_type = EventType[
                rule_data["event"]
            ]

            rule = Rule(
                name=rule_data["name"],
                event_type=event_type,
                conditions=rule_data.get(
                    "conditions",
                    {}
                ),
                action=rule_data.get(
                    "action",
                    {}
                ),
                enabled=rule_data.get(
                    "enabled",
                    True
                )
            )

            self._rules.append(rule)

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