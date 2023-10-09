from abc import abstractmethod
from collections import OrderedDict
from typing import Union

from log_analizer.core.log_engine.log import LogRaw, LogLine, LogFile
from log_analizer.core.data_dispatcher.dispatcher import Dispatcher


class BaseCollector:
    pass


class Collector:

    def __init__(self, file=None):
        self.file = file
        self._meta = {}

    @Dispatcher.update_meta
    def to_raw(self, log: str):
        Dispatcher.get_data(log, self._meta)






