from downloadVideo import downloadVideo
from getm3u8url import get_m3u8_url
from playwright.sync_api import sync_playwright
import time
from downloadImage import downloadImage
from makeDirs import makeDirs
from getConfig import getConfig


def lzparser():
    """
    Parse leakedzone.com and download videos and images
    """
    makeDirs()
    config = getConfig("config.ini")
    proxy = {"server": "45.128.135.65:1080"}
    with sync_playwright() as p:
        # Launch browser
        browser = p.firefox.launch(
            headless=False
        )  # headless=False, чтобы увидеть браузер
        page = browser.new_page()

        # Set User-Agent and Referer headers
        page.set_extra_http_headers(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Referer": "https://leakedzone.com/",
            }
        )

        page.goto(config["config"]["url"] + "/photo")

        # Scroll to bottom to load all content
        scrollToBottom(page)

        # Get all image links
        links = page.query_selector_all(".light-gallery-item > img")

        picLimit = int(config["config"]["picLimit"])
        if picLimit == -1:
            picLimit = len(links)
        for i, link in enumerate(links[:picLimit]):
            href = link.get_attribute("src")
            href = (href[: href.find("_")] + href[href.rfind(".") :]).strip()
            print(
                f"{i + 1}/{picLimit}",
                downloadImage(href, config["config"]["picFolder"]),
            )

        # Get all video urls
        vidLimit = int(config["config"]["vidLimit"])
        vidUrls = get_m3u8_url(config["config"]["url"] + "/video", page, vidLimit)
        for i, vidUrl in enumerate(vidUrls):
            print(
                f"{i + 1}/{len(vidUrls)}",
                downloadVideo(vidUrl, vidUrl.split("/")[-2] + ".mp4"),
            )


def scrollToBottom(page):
    """
    Scroll to bottom of page to load all content
    """
    last_height = page.evaluate("document.body.scrollHeight")
    while True:
        # Scroll down
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)  # Wait for content to load

        # Get new page size
        new_height = page.evaluate("document.body.scrollHeight")

        # If page size has not changed, all content is loaded
        if new_height == last_height:
            break

        last_height = new_height
