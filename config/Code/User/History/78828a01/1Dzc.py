from os import makedirs
from getConfig import getConfig


def makeDirs() -> None:
    """
    Create folders for videos and pictures
    """
    config = getConfig("config.ini")
    # Create picture folder if it does not exist
    makedirs(config["config"]["picFolder"], exist_ok=True)
    # Create video folder if it does not exist
    makedirs(config["config"]["vidFolder"], exist_ok=True)
