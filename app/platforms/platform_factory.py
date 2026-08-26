"""
==========================================================
Platform Factory
==========================================================

Назначение
----------
Создание platform-specific компонентов WinFlow.

Проект:
    WinFlow
"""

import platform

from app.platforms.process_controller import ProcessController
from app.platforms.windows.process_controller import (
    WindowsProcessController
)
from app.platforms.macos.process_controller import (
    MacOSProcessController
)


def create_process_controller() -> ProcessController:
    """
    Создаёт контроллер процессов для текущей ОС.
    """

    system = platform.system()

    if system == "Windows":
        return WindowsProcessController()

    if system == "Darwin":
        return MacOSProcessController()

    raise NotImplementedError(
        f"Platform '{system}' is not supported yet."
    )

