# coding=utf-8

import os
import sys

from workflow import Workflow

from genius import Genius
from scraper import fetch_lyrics
from utils import download_image, save_lyrics


def main(workflow):
    token = os.getenv("GENIUS_ACCESS_TOKEN", "")

    if not token:
        raise Exception(
            "Missing genius.com API token in the "
            "GENIUS_ACCESS_TOKEN env variable."
        )

    genius = Genius(token)

    text = " ".join(workflow.args).lower()

    for song in genius.search(text, per_page=3):
        lyrics = fetch_lyrics(song["url"])

        if not lyrics:
            continue

        path = song["path"].replace("/", "").replace("-lyrics", "")

        lyrics_path = save_lyrics(lyrics, name=path)
        image_path = download_image(song["header_image_url"], name=path)

        workflow.add_item(
            title=u"{title}".format(
                title=song["title"]
            ),
            subtitle=u"by {artist}".format(
                artist=song["primary_artist"]["name"]
            ),
            icon=image_path,
            arg=lyrics_path,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
