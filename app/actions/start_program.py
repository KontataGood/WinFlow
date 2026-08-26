"""
==========================================================
Start Program Action
==========================================================

Назначение
----------
Реализация действия START_PROGRAM.

Данное действие запускает указанную программу
или команду в операционной системе.

ActionDispatcher отвечает за выбор действия,
а этот класс отвечает непосредственно за его выполнение.

Проект:
    WinFlow
"""

import subprocess


class StartProgramAction:
    """
    Запускает программу.
    """

    def execute(self, action: dict):
        """
        Выполняет действие запуска программы.

        Args:
            action:
                Конфигурация действия.

                Пример:

                    {
                        "type": "START_PROGRAM",
                        "program": "notepad.exe"
                    }
        """

        program = action.get("program")

        if not program:
            return

        subprocess.Popen(
            program,
            shell=True
        )