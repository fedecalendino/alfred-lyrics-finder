from workflow import web


def download_image(url, name):
    filename = u"/tmp/{name}.png".format(name=name)

    with open(filename, "wb") as f:
        f.write(web.get(url).content)

    return f.name


def save_lyrics(lyrics, name):
    filename = u"/tmp/{name}.txt".format(name=name)

    with open(filename, "w+") as f:
        f.write("\n".join(lyrics))

    return f.name
