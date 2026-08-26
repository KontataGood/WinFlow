"""
==========================================================
Stop Program Action
==========================================================

Назначение
----------
Реализация действия STOP_PROGRAM.

Данное действие останавливает запущенную программу.

Для непосредственного взаимодействия с процессами
используется ProcessController.

Проект:
    WinFlow
"""

from app.platform.process_controller import ProcessController


class StopProgramAction:
    """
    Останавливает запущенную программу.
    """

    def __init__(
        self,
        process_controller: ProcessController
    ):
        """
        Инициализация действия.

        Args:
            process_controller:
                Контроллер процессов.
        """

        self._process_controller = process_controller

    def execute(self, action: dict):
        """
        Выполняет действие остановки программы.

        Args:
            action:
                Конфигурация действия.

                Пример:

                    {
                        "type": "STOP_PROGRAM",
                        "program": "Todo.exe"
                    }
        """

        program = action.get("program")

        if not program:
            return

        self._process_controller.stop(
            program
        )