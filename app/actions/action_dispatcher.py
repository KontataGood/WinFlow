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
from app.actions.stop_program import StopProgramAction
from app.platforms.process_controller import ProcessController
from app.actions.open_url import OpenUrlAction
from app.platforms.platform_factory import (
    create_process_controller
)

class ActionDispatcher:
    """
    Диспетчер действий WinFlow.
    """

    def __init__(self):
        """
        Инициализирует обработчики действий.
        """

        process_controller = create_process_controller()

        self._actions = {
            "START_PROGRAM": StartProgramAction(),
            "STOP_PROGRAM": StopProgramAction(
                process_controller
            ),
            "OPEN_URL": OpenUrlAction(),
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