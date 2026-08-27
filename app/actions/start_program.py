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
from app.platforms.platform_resolver import (
    PlatformResolver
)


class StartProgramAction:
    """
    Запускает приложение через platform launcher.
    """

    def __init__(self):
        self._launcher = create_program_launcher()
        self._resolver = PlatformResolver()

    def execute(self, action: dict) -> bool:

        program = self._resolver.resolve(
            action.get("program")
        )

        return self._launcher.launch(program)