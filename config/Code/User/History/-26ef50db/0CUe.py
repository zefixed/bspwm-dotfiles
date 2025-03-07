def get_m3u8_url(path, page):
    vidUrls = []

    def handle_response(response):
        if response.url.endswith("m3u8"):
            vidUrls.append(response.url)

    page.on("response", handle_response)

    page.goto(path)

    firstVid = page.query_selector(".post-thumbnail")
    firstVid.click()

    vids = page.query_selector_all(".lg-thumb-item")
    vids[1].click()
    page.wait_for_timeout(2000)
    for vid in vids[0:]:
        vid.click()
        page.wait_for_timeout(2000)

    return vidUrls
