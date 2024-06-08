# Copyright (c) AWildDevAppears

from enum import Enum


class LogLevel(Enum):
    LOG = "log"
    WARN = "warn"
    ERROR = "error"


log_history: list[tuple[LogLevel, str]] = []


def logger_log(mode: LogLevel, msg: str):
    log_history.append((mode, msg))


def log_error(msg: str):
    logger_log(LogLevel.ERROR, msg)


def log_warn(msg: str):
    logger_log(LogLevel.WARN, msg)


def log_log(msg: str):
    logger_log(LogLevel.LOG, msg)

