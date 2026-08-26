"""
==========================================================
Action Dispatcher
==========================================================

Назначение
----------
Определяет, какой обработчик необходимо использовать
для выполнения конкретного действия.

Dispatcher не содержит реализацию самих действий.

Проект:
    WinFlow
"""

from app.actions.start_program import StartProgramAction


class ActionDispatcher:
    """
    Диспетчер действий WinFlow.
    """

    def __init__(self):
        """
        Инициализирует обработчики действий.
        """

        self._actions = {
            "START_PROGRAM": StartProgramAction(),
        }

    def execute(self, action: dict):
        """
        Передает действие соответствующему обработчику.

        Args:
            action:
                Конфигурация действия.
        """

        action_type = action.get("type")

        handler = self._actions.get(action_type)

        if handler is None:
            print(
                f"Unknown action type: {action_type}"
            )
            return

        handler.execute(action)