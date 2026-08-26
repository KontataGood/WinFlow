"""
==========================================================
Process Controller
==========================================================

Назначение
----------
Абстрактный интерфейс для управления процессами.

Конкретная реализация зависит от операционной системы.

Проект:
    Autom Task
"""

from abc import ABC, abstractmethod


class ProcessController(ABC):
    """
    Абстрактный контроллер процессов.
    """

    @abstractmethod
    def stop(self, process_name: str) -> bool:
        """
        Останавливает процесс.

        Args:
            process_name:
                Имя процесса.

        Returns:
            True, если процесс был остановлен.
            False, если операция не удалась.
        """
        raise NotImplementedError