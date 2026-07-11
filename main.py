"""
==========================================================
WinFlow Entry Point
==========================================================

Точка входа приложения.

На текущем этапе:

- создаем EventBus;
- подписываем обработчик событий;
- запускаем ProcessWatcher.
"""


import time

from app.core.event import Event
from app.core.event_bus import EventBus
from app.core.event_type import EventType
from app.watchers.process_watcher import ProcessWatcher



def listener(event: Event):
    """
    Тестовый обработчик событий.

    Позже здесь будут:

    - RuleEngine;
    - Logger;
    - GUI;
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



def main():

    bus = EventBus()


    bus.subscribe(
        EventType.PROCESS_STARTED,
        listener
    )

    bus.subscribe(
        EventType.PROCESS_STOPPED,
        listener
    )


    watcher = ProcessWatcher(
        event_bus=bus,
        interval=1
    )


    watcher.start()


    print(
        "WinFlow started..."
    )


    try:

        while True:
            time.sleep(1)


    except KeyboardInterrupt:

        print(
            "Stopping WinFlow..."
        )

        watcher.stop()



if __name__ == "__main__":
    main()