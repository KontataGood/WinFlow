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
from config.config_manager import ConfigManager


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


    config = ConfigManager("configs/settings.json")
    config.load()

    watcher = ProcessWatcher(
        event_bus=bus,
        configuration=config
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