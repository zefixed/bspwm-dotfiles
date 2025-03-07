import ffmpeg
from getConfig import getConfig


def downloadVideo(url: str, output_file: str) -> str:
    config = getConfig("config.ini")
    try:
        ffmpeg.input(url).output(
            f"{config['config']['vidFolder']}/{output_file}",
            vcodec="copy",
            acodec="copy",
        ).global_args(
            "-n",
            "-loglevel",
            "warning",
        ).run()
        return f"Video saved: {output_file}"
    except ffmpeg.Error as e:
        return f"Error: {e.stderr.decode('utf8') if e.stderr else str(e)}"
