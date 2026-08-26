"""
==========================================================
Windows Program Launcher
==========================================================

Проект:
    Autom Task
"""

import subprocess

from app.platforms.program_launcher import ProgramLauncher


class WindowsProgramLauncher(ProgramLauncher):
    """
    Запуск приложений в Windows.
    """

    def launch(self, program: str) -> bool:

        if not program:
            return False

        try:
            subprocess.Popen(
                program,
                shell=True
            )

            return True

        except OSError:
            return False