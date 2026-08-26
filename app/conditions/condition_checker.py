"""
==========================================================
Condition Checker
==========================================================

Назначение
----------
Проверка условий правила относительно данных события.

Проект:
    Autom Task
"""

from app.conditions.condition import Condition
from app.conditions.condition_operator import ConditionOperator


class ConditionChecker:
    """
    Проверяет условия автоматизации.
    """

    def check(
        self,
        conditions: list[Condition],
        event_data: dict
    ) -> bool:
        """
        Проверяет все условия.

        Все условия должны быть выполнены.

        Args:
            conditions:
                Список условий.

            event_data:
                Данные события.

        Returns:
            True, если все условия выполнены.
        """

        for condition in conditions:

            actual_value = event_data.get(
                condition.field
            )

            if not self._check_condition(
                condition,
                actual_value
            ):
                return False

        return True

    def _check_condition(
        self,
        condition: Condition,
        actual_value: object
    ) -> bool:

        if condition.operator == ConditionOperator.EQUALS:
            return actual_value == condition.value

        if condition.operator == ConditionOperator.NOT_EQUALS:
            return actual_value != condition.value

        if condition.operator == ConditionOperator.CONTAINS:

            if not isinstance(actual_value, str):
                return False

            return condition.value in actual_value

        if condition.operator == ConditionOperator.STARTS_WITH:

            if not isinstance(actual_value, str):
                return False

            return actual_value.startswith(
                condition.value
            )

        return False