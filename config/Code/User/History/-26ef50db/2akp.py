def get_m3u8_url(path: str, page: object, limit: int) -> list:
    """
    Get all m3u8 urls from a webpage
    """
    vidUrls = []

    def handle_response(response):
        """
        Handle response event
        """
        if response.url.endswith("m3u8"):
            vidUrls.append(response.url)

    # set up response event handler
    page.on("response", handle_response)

    page.goto(path)

    # get first video
    firstVid = page.query_selector(".post-thumbnail")
    # click first video
    page.wait_for_timeout(2000)
    firstVid.click()

    # get all videos
    vids = page.query_selector_all(".lg-thumb-item")
    # click second video to skip advertisment
    vids[1].click()
    page.wait_for_timeout(2000)

    if limit == -1:
        limit = len(vids)

    # click all other videos
    for vid in vids[0:limit]:
        vid.click()
        page.wait_for_timeout(2000)

    # return list of urls
    return vidUrls
