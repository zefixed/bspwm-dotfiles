from downloadVideo import downloadVideo
from getm3u8url import get_m3u8_url
from playwright.sync_api import sync_playwright
import time
from downloadImage import downloadImage
from makeDirs import makeDirs
from getConfig import getConfig


def lzparser():
    makeDirs()
    config = getConfig("config.ini")
    with sync_playwright() as p:
        # Запускаем браузер
        browser = p.firefox.launch(
            headless=False
        )  # headless=False, чтобы увидеть браузер
        page = browser.new_page()

        # Устанавливаем заголовки User-Agent и Referer
        page.set_extra_http_headers(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Referer": "https://leakedzone.com/",
            }
        )

        page.goto(config["config"]["url"] + "photo")

        scrollToBottom(page)

        links = page.query_selector_all(".light-gallery-item > img")

        for link in links:
            href = link.get_attribute("src")
            href = (href[: href.find("_")] + href[href.rfind(".") :]).strip()
            downloadImage(href, config["config"]["picFolder"])

        for vidUrl in get_m3u8_url(config["config"]["url"] + "video", page):
            downloadVideo(vidUrl, vidUrl.split("/")[-2] + ".mp4")


def scrollToBottom(page):
    last_height = page.evaluate("document.body.scrollHeight")
    while True:
        # Прокручиваем вниз
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)  # Ждем, пока контент подгрузится

        # Получаем новый размер страницы
        new_height = page.evaluate("document.body.scrollHeight")

        # Если размер страницы не изменился, значит весь контент подгружен
        if new_height == last_height:
            break

        last_height = new_height
