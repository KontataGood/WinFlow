"""
==========================================================
Condition Checker
==========================================================

Назначение
----------
Проверка условий правила относительно полученного события.

ConditionChecker отделяет логику проверки условий
от RuleEngine.

На текущем этапе поддерживается простое сравнение:

    actual_value == expected_value

Все условия одного правила должны быть выполнены.

Проект:
    WinFlow
"""


class ConditionChecker:
    """
    Проверяет условия автоматизации.
    """

    def check(
        self,
        conditions: dict,
        event_data: dict
    ) -> bool:
        """
        Проверяет все условия.

        Args:
            conditions:
                Условия правила.

            event_data:
                Данные полученного события.

        Returns:
            True, если все условия выполнены.
            False, если хотя бы одно условие
            не выполнено.
        """

        for key, expected_value in conditions.items():

            actual_value = event_data.get(key)

            if actual_value != expected_value:
                return False

        return True