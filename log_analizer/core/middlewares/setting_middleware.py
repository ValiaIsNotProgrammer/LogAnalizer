import os
from pathlib import Path, PurePath
from typing import Union

from log_analizer import settings


class Settings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __is_settings_file_exists(self, path: PurePath) -> bool:
        if os.path.exists(path):
            return True
        return False

    def __is_param_settings_exists(self) -> bool:
        pass

    def __is_correct_param_settings(self) -> bool:
        pass

    def _get_settings_file_path(self) -> Path:
        package_directory = Path(__file__).resolve().parent.parent.parent
        settings_path = package_directory / 'settings.py'
        if self.__is_settings_file_exists(settings_path):
            return settings_path
        raise Exception("Error")


class SettingsProvider(Settings):

    def __init__(self):
        # self.settings_path: Path = self._get_settings_file_path()
        pass

    @staticmethod
    def get_custom_middlewares(key) -> Union[list, str, int]:
        if SettingsProvider.__is_valid_key(settings.MIDDLEWARES, key):
            return settings.MIDDLEWARES[key]
        raise Exception(f"Error key {key} in settings map {map}")

    @staticmethod
    def __is_valid_key(map: dict, key: Union[str, int]):
        if key in map.keys():
            return True
        return False




class SettingsApplier(Settings):
    pass

