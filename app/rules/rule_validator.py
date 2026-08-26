"""
==========================================================
Rule Validator
==========================================================

Назначение
----------
Проверка корректности конфигурации правила перед его
преобразованием в объект Rule.

Validator отвечает только за проверку структуры данных.

Проект:
    WinFlow
"""


class RuleValidationError(Exception):
    """
    Ошибка некорректной конфигурации правила.
    """


class RuleValidator:
    """
    Проверяет конфигурацию правила.
    """

    def validate(self, rule: dict):
        """
        Проверяет правило.

        Args:
            rule:
                Конфигурация правила.

        Raises:
            RuleValidationError:
                Если конфигурация некорректна.
        """

        self._validate_name(rule)
        self._validate_event(rule)
        self._validate_conditions(rule)
        self._validate_actions(rule)

    def _validate_name(self, rule: dict):

        if not isinstance(rule.get("name"), str):
            raise RuleValidationError(
                "Rule name must be a string"
            )

    def _validate_event(self, rule: dict):

        if not isinstance(rule.get("event"), str):
            raise RuleValidationError(
                f"Invalid event in rule "
                f"'{rule.get('name')}'"
            )

    def _validate_conditions(self, rule: dict):

        conditions = rule.get("conditions")

        if not isinstance(conditions, list):
            raise RuleValidationError(
                f"Conditions must be a list "
                f"in rule '{rule.get('name')}'"
            )

        for condition in conditions:

            if not isinstance(condition, dict):
                raise RuleValidationError(
                    f"Invalid condition in rule "
                    f"'{rule.get('name')}'"
                )

            required = (
                "field",
                "operator",
                "value"
            )

            for key in required:
                if key not in condition:
                    raise RuleValidationError(
                        f"Missing '{key}' in condition "
                        f"of rule '{rule.get('name')}'"
                    )

    def _validate_actions(self, rule: dict):

        actions = rule.get("actions")

        if not isinstance(actions, list):
            raise RuleValidationError(
                f"Actions must be a list "
                f"in rule '{rule.get('name')}'"
            )

        for action in actions:

            if not isinstance(action, dict):
                raise RuleValidationError(
                    f"Invalid action in rule "
                    f"'{rule.get('name')}'"
                )

            if "type" not in action:
                raise RuleValidationError(
                    f"Action type is missing "
                    f"in rule '{rule.get('name')}'"
                )