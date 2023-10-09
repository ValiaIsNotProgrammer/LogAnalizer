import inspect
from abc import ABC
from pathlib import Path
from typing import Union

from log_analizer.core.log_engine.log import LogRaw, LogFile, LogLine
from setting_middleware import SettingsProvider


class BaseMiddleware(ABC):
    
    CUSTOM_MIDDLEWARE_KEY = None

    def checkup(self, value):
        method_validators = [name for name, member in inspect.getmembers(self, inspect.ismethod)
                             if name.endswith('validator')]
        custom_validator = self.get_custom_middleware()

        for method_name in method_validators + custom_validator:
            validator = getattr(self, method_name)
            if not validator(value):
                raise Exception("Ошибка валидации")
            return value

    @classmethod
    def get_custom_middleware(cls):
        if cls.CUSTOM_MIDDLEWARE_KEY is None:
            print(f"Не удалось подключить middleware из-за отсутсвия CUSTOM_MIDDLEWARE_KEY в {cls.__name__}")
            return []
        return SettingsProvider.get_custom_middlewares(cls.CUSTOM_MIDDLEWARE_KEY)


class LogRawMiddleware(BaseMiddleware):
    CUSTOM_MIDDLEWARE_KEY = "LogRaw"

    def type_validator(self, value) -> bool:
        if type(value) == LogRaw:
            return True
        return False


class LogLineMiddleware(BaseMiddleware):
    pass


class LogFileMiddleware(BaseMiddleware):
    pass
