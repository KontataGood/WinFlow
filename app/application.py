"""
application.py

Главный класс приложения Autom Task.

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
from app.logger.logger import Logger
from app.core.event_bus import EventBus
from app.watchers.process_watcher import ProcessWatcher
from app.rules.rule_manager import RuleManager
from app.rules.rule_engine import RuleEngine

class Application:
    """
    Главный класс Autom Task.

    Создает все основные компоненты приложения и
    управляет их жизненным циклом.
    """

    def __init__(self):
        """Инициализация приложения."""

        # ---------- Configuration ----------

        self._configuration = ConfigManager("configs/settings.json")
        self._configuration.load()

        # ---------- Rule Manager ----------

        self._rule_manager = RuleManager(
            self._configuration
        )

        # ---------- Core ----------

        self._event_bus = EventBus()

        # ---------- Rule Engine ----------

        self._rule_engine = RuleEngine(
            event_bus=self._event_bus,
            rule_manager=self._rule_manager
        )

        # ---------- Watchers ----------

        self._process_watcher = ProcessWatcher(
            event_bus=self._event_bus,
            configuration=self._configuration
        )

        # ---------- Logger ----------

        self._logger = Logger(
            self._event_bus
        )

    def run(self):
        """
        Запускает приложение.

        Здесь запускаются все сервисы,
        которые должны работать постоянно.
        """

        print("Autom Task started...")

        self._process_watcher.start()

    def stop(self):
        """
        Корректно завершает работу приложения.
        """

        print("Stopping Autom Task...")

        self._process_watcher.stop()