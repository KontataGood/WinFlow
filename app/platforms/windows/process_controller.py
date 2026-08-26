"""
==========================================================
Windows Process Controller
==========================================================

Назначение
----------
Windows-реализация ProcessController.

Проект:
    Autom Task
"""

import subprocess

from app.platforms.process_controller import ProcessController


class WindowsProcessController(ProcessController):
    """
    Контроллер процессов для Windows.
    """

    def stop(self, process_name: str) -> bool:
        """
        Останавливает Windows-процесс через taskkill.

        Args:
            process_name:
                Имя процесса.

        Returns:
            True, если процесс был остановлен.
            False, если операция завершилась ошибкой.
        """

        if not process_name:
            return False

        try:
            subprocess.run(
                [
                    "taskkill",
                    "/IM",
                    process_name,
                    "/F"
                ],
                check=True,
                capture_output=True,
                text=True
            )

            return True

        except subprocess.CalledProcessError:
            return False