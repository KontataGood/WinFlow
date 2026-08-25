"""
logger.py

Система логирования WinFlow.

Logger получает события через EventBus
и сохраняет информацию о работе приложения.
"""
import logging

from pathlib import Path

from app.core.event import Event
from app.core.event_type import EventType


class Logger:
    """
    Логгер приложения.

    Отвечает за запись событий WinFlow.
    """

    def __init__(self, event_bus):
        """
        Инициализация Logger.

        Args:
            event_bus:
                Шина событий приложения.
        """

        self._event_bus = event_bus

        self._logger = self._create_logger()

        self._register_events()


    def _create_logger(self):
        """
        Создает объект стандартного Python logger.
        """

        log_directory = Path("logs")

        log_directory.mkdir(
            exist_ok=True
        )

        logger = logging.getLogger("WinFlow")

        logger.setLevel(logging.INFO)


        # Чтобы при повторном создании
        # не добавлять обработчики снова
        if not logger.handlers:

            file_handler = logging.FileHandler(
                log_directory / "winflow.log",
                encoding="utf-8"
            )

            console_handler = logging.StreamHandler()


            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )


            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)


            logger.addHandler(file_handler)
            logger.addHandler(console_handler)


        return logger


    def _register_events(self):
        """
        Подписка на события приложения.
        """

        self._event_bus.subscribe_all(
            self._handle_event
        )


    def _handle_event(self, event: Event):
        """
        Обработка события.

        Любое событие превращается в запись лога.
        """

        self._logger.info(
            f"{event.type.name} | "
            f"{event.data}"
        )