"""
==========================================================
Action Dispatcher
==========================================================

Назначение
----------
ActionDispatcher отвечает за выполнение действий,
описанных в правилах WinFlow.

RuleEngine определяет, какое правило подходит
под событие, а ActionDispatcher выполняет
указанное в правиле действие.

Пример:

    RuleEngine
        │
        ▼
    ActionDispatcher
        │
        ▼
    START_PROGRAM
        │
        ▼
    spotify.exe

Проект:
    WinFlow
"""

import subprocess


class ActionDispatcher:
    """
    Выполняет действия WinFlow.
    """

    def execute(self, action: dict):
        """
        Выполняет действие.

        Args:
            action:
                Словарь с описанием действия.
        """

        action_type = action.get("type")

        if action_type == "START_PROGRAM":
            self._start_program(action)

    @staticmethod
    def _start_program(action: dict):
        """
        Запускает программу.

        Args:
            action:
                Описание действия START_PROGRAM.
        """

        program = action.get("program")

        if not program:
            return

        subprocess.Popen(
            program,
            shell=True
        )