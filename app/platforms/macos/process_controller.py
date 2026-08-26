"""
==========================================================
macOS Process Controller
==========================================================

Назначение
----------
macOS-реализация ProcessController.

Проект:
    Autom Task
"""

import subprocess

from app.platforms.process_controller import ProcessController


class MacOSProcessController(ProcessController):
    """
    Контроллер процессов для macOS.
    """

    def stop(self, process_name: str) -> bool:
        """
        Останавливает процесс по имени.

        Args:
            process_name:
                Имя процесса.

        Returns:
            True, если команда завершилась успешно.
            False, если процесс не найден или произошла ошибка.
        """

        if not process_name:
            return False

        try:
            subprocess.run(
                [
                    "pkill",
                    "-x",
                    process_name
                ],
                check=True,
                capture_output=True,
                text=True
            )

            return True

        except subprocess.CalledProcessError:
            return False