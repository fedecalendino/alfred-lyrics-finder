import os

from workflow import web

IMAGE_FILENAME = u"/tmp/{name}.png"
LYRICS_FILENAME = u"/tmp/{name}.txt"


def load_image(name):
    filename = IMAGE_FILENAME.format(name=name)
    return filename if os.path.isfile(filename) else None


def load_lyrics(name):
    filename = LYRICS_FILENAME.format(name=name)
    return filename if os.path.isfile(filename) else None


def download_image(url, name):
    filename = load_image(name)

    if filename:
        return filename

    filename = IMAGE_FILENAME.format(name=name)

    with open(filename, "wb") as f:
        f.write(web.get(url).content)

    return f.name


def save_lyrics(lyrics, name):
    filename = LYRICS_FILENAME.format(name=name)

    with open(filename, "w+") as f:
        f.write("\n".join(lyrics))

    return f.name

