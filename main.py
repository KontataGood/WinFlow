"""
==========================================================
WinFlow
==========================================================

Точка входа в приложение.

На текущем этапе main.py используется
для тестирования компонентов ядра.

В дальнейшем здесь будет происходить:

- загрузка конфигурации;
- создание EventBus;
- запуск Watchers;
- запуск RuleEngine;
- запуск GUI;
- корректное завершение приложения.
"""

from app.core.event import Event
from app.core.event_bus import EventBus
from app.core.event_type import EventType


def listener(event: Event):
    print(f"Получено событие: {event.type.name}")
    print(event.data)


bus = EventBus()

bus.subscribe(
    EventType.PROCESS_STARTED,
    listener
)

bus.publish(
    Event(
        type=EventType.PROCESS_STARTED,
        source="Test",
        data={
            "process": "steam.exe"
        }
    )
)