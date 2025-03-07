import httplib2


def downloadImage(url: str, save_path: str) -> str:
    """
    Download image from url and save it to save_path
    """
    try:
        # Create a cache directory if it does not exist
        h = httplib2.Http(".cache")
        # Request image url
        response, content = h.request(url)
        # Open a file for writing with the same name as the url
        out = open(f"{save_path}/{url.split('/')[-1]}", "wb")
        # Write the content to the file
        out.write(content)
        # Close the file
        out.close()
        # Return a success message
        return f"Downloaded: {url}"
    except Exception as e:
        # Return an error message
        return f"Error: {url}, {str(e)}"
