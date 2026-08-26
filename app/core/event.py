"""
==========================================================
Event
==========================================================

Назначение
----------
Определяет универсальный объект события,
используемый всеми компонентами Autom Task.

Каждое событие содержит одинаковый набор данных,
независимо от его типа.

Например:

PROCESS_STARTED

↓

Event

↓

RuleEngine

↓

Logger

↓

GUI

Это позволяет всем компонентам работать
с единым интерфейсом.

Пример использования
--------------------

Event(
    type=EventType.PROCESS_STARTED,
    source="ProcessWatcher",
    data={
        "process": "steam.exe"
    }
)
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.core.event_type import EventType


@dataclass(slots=True)
class Event:
    """
    Универсальная модель события.

    Хранит информацию о произошедшем событии,
    его источнике, дополнительных данных
    и времени возникновения.

    Event является основным объектом,
    который передается через EventBus.
    """

    # Тип произошедшего события
    type: EventType

    # Источник события (например ProcessWatcher)
    source: str

    # Дополнительная информация
    data: dict[str, Any] = field(default_factory=dict)
    
    # Время создания события
    timestamp: datetime = field(default_factory=datetime.now)