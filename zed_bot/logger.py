"""Simple logging module."""
import logging

from zed_bot.enums import IS_LOCAL


def get_logger(name: str = None):
    kwargs = {}
    if name:
        kwargs.update({name: name})
    if IS_LOCAL:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        filename="./logs/zed_bot.log",
        level=level,
        filemode="w",
        format="%(levelname)s:%(name)s:%(filename)s:%(funcName)s:%(asctime)s:%(message)s",
    )
    logger = logging.getLogger(**kwargs)
    return logger
