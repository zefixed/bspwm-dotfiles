import httplib2


def downloadImage(url: str, save_path: str) -> str:
    try:
        h = httplib2.Http(".cache")
        response, content = h.request(url)
        out = open(f"{save_path}/{url.split("/")[-1]}", "wb")
        out.write(content)
        out.close()
        return f"Downloaded: {url}"
    except Exception as e:
        return f"Error: {url}, {str(e)}"
