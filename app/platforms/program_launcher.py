"""
==========================================================
Program Launcher
==========================================================

Назначение
----------
Абстрактный интерфейс для запуска приложений.

Конкретная реализация зависит от операционной системы.

Проект:
    WinFlow
"""

from abc import ABC, abstractmethod


class ProgramLauncher(ABC):
    """
    Абстрактный интерфейс запуска приложений.
    """

    @abstractmethod
    def launch(self, program: str) -> bool:
        """
        Запускает приложение.

        Args:
            program:
                Имя приложения.

        Returns:
            True, если запуск выполнен успешно.
            False, если произошла ошибка.
        """
        raise NotImplementedError