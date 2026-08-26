"""
==========================================================
Condition
==========================================================

Назначение
----------
Модель одного условия правила.

Условие состоит из:

    field
    operator
    value

Пример:

    {
        "field": "process",
        "operator": "equals",
        "value": "Todo.exe"
    }

Проект:
    WinFlow
"""

from dataclasses import dataclass

from app.conditions.condition_operator import ConditionOperator


@dataclass(frozen=True)
class Condition:
    """
    Представляет одно условие правила.
    """

    field: str
    operator: ConditionOperator
    value: object