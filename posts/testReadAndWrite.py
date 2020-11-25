import requests


def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg","image/svg+xml")
    try:
        r = requests.head(image_url)
        if r.headers["content-type"] in image_formats:
            return True

        else:
            return False;

    except:
        return False;




image=is_url_image("https://www.ndtv.com/")
print(image)