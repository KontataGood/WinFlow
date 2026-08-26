"""
==========================================================
Condition Operators
==========================================================

Назначение
----------
Перечисление операторов, используемых при проверке условий.

Проект:
    WinFlow
"""

from enum import Enum


class ConditionOperator(Enum):
    """
    Операторы сравнения условий.
    """

    EQUALS = "equals"
    NOT_EQUALS = "not_equals"
    CONTAINS = "contains"
    STARTS_WITH = "starts_with"