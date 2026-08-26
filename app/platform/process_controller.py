"""
==========================================================
Process Controller
==========================================================

Назначение
----------
Абстракция для управления процессами операционной системы.

ProcessController предоставляет единый интерфейс для
компонентов WinFlow, которым необходимо взаимодействовать
с процессами.

Компоненты верхнего уровня не должны напрямую использовать
platform-specific команды вроде taskkill, kill и т.д.

В будущем реализация может быть разделена по платформам:

    Windows
    macOS
    Linux

Проект:
    WinFlow
"""

import subprocess


class ProcessController:
    """
    Базовый контроллер процессов.

    Предоставляет операции, необходимые WinFlow
    для управления запущенными процессами.
    """

    def stop(self, process_name: str):
        """
        Останавливает процесс по имени.

        Args:
            process_name:
                Имя процесса, который необходимо остановить.

        Returns:
            True, если команда завершилась успешно.
            False, если произошла ошибка.
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