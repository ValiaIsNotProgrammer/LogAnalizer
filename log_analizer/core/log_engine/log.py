from pathlib import Path


class LogRaw(str):
    pass


class LogLine:

    def __init__(self, log: str):
        pass

    def convert_to_line(self, log: LogRaw):
        pass


class LogFile:

    def __init__(self, log_path: Path):
        pass


