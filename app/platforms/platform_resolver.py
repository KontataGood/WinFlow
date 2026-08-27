"""
==========================================================
Platform Resolver
==========================================================

Назначение
----------
Разрешает platform-specific значения конфигурации.

Например:

    {
        "windows": "chrome.exe",
        "macos": "Google Chrome"
    }

На Windows будет выбрано:
    chrome.exe

На macOS:
    Google Chrome

Проект:
    Autom Task
"""

import platform


class PlatformResolver:
    """
    Разрешает значения в зависимости от текущей ОС.
    """

    def __init__(self):
        system = platform.system()

        if system == "Windows":
            self._platform = "windows"

        elif system == "Darwin":
            self._platform = "macos"

        else:
            raise NotImplementedError(
                f"Platform '{system}' is not supported yet."
            )

    def resolve(self, value):
        """
        Возвращает значение для текущей платформы.

        Если значение не является platform-specific
        словарём, оно возвращается без изменений.
        """

        if not isinstance(value, dict):
            return value

        if self._platform in value:
            return value[self._platform]

        return value