"""
==========================================================
Event Bus
==========================================================

Назначение
----------
Центральная система обмена событиями между компонентами
приложения.

Основная идея
-------------
Компоненты приложения не должны знать друг о друге.

Например:

ProcessWatcher

    │

    ▼

EventBus

    │

    ├── RuleEngine
    ├── Logger
    ├── GUI
    └── Plugins

Таким образом Watcher публикует событие,
не зная, кто будет его получать.

Ответственность
---------------
- регистрация подписчиков;
- удаление подписчиков;
- публикация событий.

Не отвечает за:
---------------
- выполнение действий;
- проверку правил;
- хранение конфигурации.

Автор:
    Kontata

Проект:
    Autom Task
"""
from collections import defaultdict
from collections.abc import Callable

from app.core.event import Event
from app.core.event_type import EventType


class EventBus:
    """
    Центральная шина событий приложения.

    EventBus реализует паттерн Publish / Subscribe.

    Любой компонент может:

        • подписаться на событие;
        • отписаться;
        • опубликовать событие.

    Благодаря этому достигается слабая связанность
    компонентов приложения.

    Пример использования
    --------------------

    bus.subscribe(
        EventType.PROCESS_STARTED,
        callback
    )

    bus.publish(event)
    """

    def __init__(self):
        self._global_subscribers = []
        self._subscribers = defaultdict(list)

    def subscribe(
        self,
        event_type: EventType,
        callback: Callable[[Event], None]
    ):
        """
        Подписывает callback на определенный тип события.

        Callback будет вызван только тогда,
        когда EventBus получит событие указанного типа.

        Args:
            event_type:
                Тип события, на которое производится подписка.

            callback:
                Функция или метод, который будет вызван
                при получении события.
        """

        self._subscribers[event_type].append(callback)


    def subscribe_all(
        self,
        callback: Callable[[Event], None]
    ):
        """
        Подписывает callback на все события.

        В отличие от subscribe(), callback будет
        получать события любого типа.

        Это удобно для компонентов, которым необходимо
        наблюдать за всей системой.

        Например:

            Logger
            Monitoring
            Debugger
        """

        self._global_subscribers.append(callback)

    def unsubscribe(
        self,
        event_type: EventType,
        callback: Callable[[Event], None]
    ):
        """
        Удаляет callback из подписчиков события.

        Если callback не был подписан,
        ничего не происходит.

        Args:
            event_type:
                Тип события.

            callback:
                Обработчик, который необходимо удалить.
        """

        if callback in self._subscribers[event_type]:
            self._subscribers[event_type].remove(callback)

    def publish(self, event: Event):
        """
        Публикует событие в системе.

        Сначала событие получают подписчики,
        зарегистрированные для конкретного типа события.

        Затем событие получают глобальные подписчики,
        подписанные через subscribe_all().

        EventBus не знает, что именно делают
        получатели события.
        """

        for callback in self._subscribers[event.type]:
            callback(event)

        for callback in self._global_subscribers:
            callback(event)