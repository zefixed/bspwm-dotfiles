from configparser import ConfigParser
from os import makedirs
from getConfig import getConfig


def makeDirs() -> None:
    config = getConfig("config.ini")
    makedirs(config["config"]["picFolder"], exist_ok=True)
    makedirs(config["config"]["vidFolder"], exist_ok=True)
