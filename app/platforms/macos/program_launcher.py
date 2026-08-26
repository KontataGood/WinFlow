"""
==========================================================
macOS Program Launcher
==========================================================

Проект:
    WinFlow
"""

import subprocess

from app.platforms.program_launcher import ProgramLauncher


class MacOSProgramLauncher(ProgramLauncher):
    """
    Запуск приложений в macOS.
    """

    def launch(self, program: str) -> bool:

        if not program:
            return False

        try:
            subprocess.Popen(
                [
                    "open",
                    "-a",
                    program
                ]
            )

            return True

        except OSError:
            return False