import re
import requests


def get_random_image() -> list[str]:
    url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(url)
    data = r.json()
    # extract breed name
    match = re.findall(r'breeds/([^/]+)/', data["message"])
    match: str = match[0]

    return [match.capitalize(), data["message"]]


def get_random_images(n=2) -> list[dict]:
    result = []
    url = f"https://dog.ceo/api/breeds/image/random/{n}"
    r = requests.get(url)
    data = r.json()["message"]

    for row in data:
        match = re.findall(r'breeds/([^/]+)/', row)
        match: str = match[0]
        result.append({"breed": match, "img": row})

    return result




if __name__ == "__main__":
    print(get_random_image())
    print(get_random_images(3))