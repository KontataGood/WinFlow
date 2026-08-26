"""
==========================================================
Start Program Action
==========================================================

Проект:
    Autom Task
"""

from app.platforms.platform_factory import (
    create_program_launcher
)


class StartProgramAction:
    """
    Запускает приложение через platform launcher.
    """

    def __init__(self):
        self._launcher = create_program_launcher()

    def execute(self, action: dict) -> bool:

        program = action.get("program")

        return self._launcher.launch(program)