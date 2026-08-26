"""
==========================================================
Platform Factory
==========================================================

Назначение
----------
Создание platform-specific компонентов Autom Task.

Проект:
    Autom Task
"""

import platform

from app.platforms.process_controller import ProcessController
from app.platforms.windows.process_controller import (
    WindowsProcessController
)
from app.platforms.macos.process_controller import (
    MacOSProcessController
)
from app.platforms.program_launcher import ProgramLauncher

from app.platforms.windows.program_launcher import (
    WindowsProgramLauncher
)

from app.platforms.macos.program_launcher import (
    MacOSProgramLauncher
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

def create_program_launcher() -> ProgramLauncher:
    """
    Создаёт launcher для текущей ОС.
    """

    system = platform.system()

    if system == "Windows":
        return WindowsProgramLauncher()

    if system == "Darwin":
        return MacOSProgramLauncher()

    raise NotImplementedError(
        f"Platform '{system}' is not supported yet."
    )
