import requests
from slugify import slugify
import sys


PEXELS_API_KEY = "wdGUIbkWmQNhDlp5JfhThsGcokdPewgqqNHYwiiw4E1oA9cBAtYqoosM"


def fetch_image(topic):

    slug = slugify(topic)

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    query = f"cybersecurity {topic}"

    url = f"https://api.pexels.com/v1/search?query={query}&per_page=5"

    response = requests.get(url, headers=headers)

    data = response.json()

    if not data["photos"]:
        return None

    image_url = data["photos"][0]["src"]["large"]

    img_data = requests.get(image_url).content

    image_path = f"static/images/{slug}.jpg"

    with open(image_path, "wb") as f:
        f.write(img_data)

    return f"/images/{slug}.jpg"


if __name__ == "__main__":
    topic = sys.argv[1]
    print(fetch_image(topic))
