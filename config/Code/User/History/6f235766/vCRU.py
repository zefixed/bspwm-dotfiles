import ffmpeg
from getConfig import getConfig


def downloadVideo(url: str, output_file: str) -> str:
    # Load configuration settings from config.ini
    config = getConfig("config.ini")
    try:
        # Use ffmpeg to download the video from the URL and save it to the specified output file
        ffmpeg.input(url).output(
            f"{config['config']['vidFolder']}/{output_file}",  # Save path
            vcodec="copy",  # Copy video codec
            acodec="copy",  # Copy audio codec
        ).global_args(
            "-n",  # Do not overwrite existing files
            "-loglevel",
            "warning",  # Set log level to warning
        ).run()
        # Return success message upon successful download
        return f"Video saved: {output_file}"
    except ffmpeg.Error as e:
        # Return error message if download fails
        return f"Error: {e.stderr.decode('utf8') if e.stderr else str(e)}"
