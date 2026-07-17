import json

class ConfigManager:

    def __init__(self, config_path: str):
        self._config_path = config_path
        self._config = {}

    def load(self):

        with open(
            self._config_path,
            "r",
            encoding="utf-8"
        ) as file:

            self._config = json.load(file)

    def save(self):
        ...

    def get(self, path: str, default=None):

        keys = path.split(".")

        value = self._config

        for key in keys:

            if not isinstance(value, dict):
                return default

            if key not in value:
                return default

            value = value[key]

        return value

    def set(self, path: str, value):
        ...