"""
==========================================================
Process Watcher
==========================================================

Назначение
----------
Отслеживает запуск и завершение процессов Windows.

ProcessWatcher является источником событий
для системы WinFlow.

Он НЕ выполняет действий.

Его задача:

Windows процессы

        ↓

Обнаружение изменений

        ↓

Создание Event

        ↓

Отправка в EventBus


Использует:
-----------
psutil
для получения списка процессов.


Генерируемые события:
---------------------

PROCESS_STARTED

PROCESS_STOPPED
"""


import time

import psutil
import threading

from app.core.event import Event
from app.core.event_bus import EventBus
from app.core.event_type import EventType
from app.core.watcher import Watcher



class ProcessWatcher(Watcher):
    """
    Наблюдатель за процессами Windows.

    Отслеживает:

    - появление новых процессов;
    - завершение процессов.
    """


    def __init__(
        self,
        event_bus: EventBus,
        interval: int = 1
    ):
        """
        Создает ProcessWatcher.

        Parameters
        ----------
        event_bus:
            Шина событий приложения.

        interval:
            Интервал проверки процессов
            в секундах.
        """

        self.event_bus = event_bus
        self.interval = interval

        self.running = False

        self.thread = None

        self.processes = set()


    def start(self):
        """
        Запускает мониторинг процессов
        в отдельном потоке.
        """

        if self.running:
            return

        self.running = True

        self.processes = self._get_processes()

        self.thread = threading.Thread(
            target=self._run,
            daemon=True
        )

        self.thread.start()


    def _run(self):
        """
        Основной цикл наблюдения.

        Выполняется внутри отдельного потока.
        """
        while self.running:
            self._check_processes()
            time.sleep(self.interval)

    def stop(self):
        """
        Останавливает мониторинг.
        """

        self.running = False


    @staticmethod
    def _get_processes() -> set[str]:
        """
        Получает текущий список процессов.

        Возвращает:
            set имен процессов
        """

        processes = set()

        for process in psutil.process_iter(
            ["name"]
        ):
            try:
                processes.add(
                    process.info["name"]
                )

            except psutil.NoSuchProcess:
                pass


        return processes



    def _check_processes(self):
        """
        Сравнивает старый список процессов
        с текущим.
        """

        current = self._get_processes()


        started = current - self.processes

        stopped = self.processes - current


        for process in started:

            self.event_bus.publish(
                Event(
                    type=EventType.PROCESS_STARTED,
                    source="ProcessWatcher",
                    data={
                        "process": process
                    }
                )
            )


        for process in stopped:

            self.event_bus.publish(
                Event(
                    type=EventType.PROCESS_STOPPED,
                    source="ProcessWatcher",
                    data={
                        "process": process
                    }
                )
            )


        self.processes = current