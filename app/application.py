"""
application.py

Главный класс приложения WinFlow.

Отвечает за:

- создание всех компонентов приложения;
- их инициализацию;
- регистрацию обработчиков событий;
- запуск и остановку сервисов.

Application НЕ содержит бизнес-логику.

Его задача — собрать все части приложения вместе
и управлять их жизненным циклом.
"""

from config.config_manager import ConfigManager
from app.core.event import Event
from app.core.event_bus import EventBus
from app.core.event_type import EventType
from app.watchers.process_watcher import ProcessWatcher


class Application:
    """
    Главный класс WinFlow.

    Создает все основные компоненты приложения и
    управляет их жизненным циклом.
    """

    def __init__(self):
        """Инициализация приложения."""

        # ---------- Configuration ----------

        self._configuration = ConfigManager("configs/settings.json")
        self._configuration.load()

        # ---------- Core ----------

        self._event_bus = EventBus()

        # ---------- Watchers ----------

        self._process_watcher = ProcessWatcher(
            event_bus=self._event_bus,
            configuration=self._configuration
        )

        # ---------- Registration ----------

        self._register_handlers()

    def run(self):
        """
        Запускает приложение.

        Здесь запускаются все сервисы,
        которые должны работать постоянно.
        """

        print("WinFlow started...")

        self._process_watcher.start()

    def stop(self):
        """
        Корректно завершает работу приложения.
        """

        print("Stopping WinFlow...")

        self._process_watcher.stop()

    def _register_handlers(self):
        """
        Регистрирует обработчики событий.

        В дальнейшем сюда будут добавляться
        новые события и новые подписчики.
        """

        self._event_bus.subscribe(
            EventType.PROCESS_STARTED,
            self._listener
        )

        self._event_bus.subscribe(
            EventType.PROCESS_STOPPED,
            self._listener
        )

    @staticmethod
    def _listener(event: Event):
        """
        Временный обработчик событий.

        Позже будет заменен системой логирования
        или RuleEngine.
        """

        print(
            f"""
[EVENT]

Type:
{event.type.name}

Source:
{event.source}

Data:
{event.data}
"""
        )