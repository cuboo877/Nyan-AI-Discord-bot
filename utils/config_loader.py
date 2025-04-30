# utils/config_loader.py
import json

class ConfigLoader:
    _config = None  # ← 類別層級變數，全專案共用！

    @classmethod
    def load(cls):
        try:
            with open('config.json', 'r', encoding='utf-8') as file:
                cls._config = json.load(file)
        except FileNotFoundError:
            raise Exception("Can't find config file")
        except json.JSONDecodeError as e:
            raise Exception(f"JSON syntax error: {e}")

    @classmethod
    def get(cls, key, default=None):
        if cls._config is None:
            raise Exception("Config not loaded! Did you forget to call ConfigLoader.load()? (；ω；)")
        return cls._config.get(key, default)
