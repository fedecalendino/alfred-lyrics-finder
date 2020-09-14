# coding=utf-8

import os
import sys

from workflow import Workflow

from genius import Genius
from scraper import fetch_lyrics
from utils import download_image, save_lyrics


def main(workflow):
    url = workflow.args[0]
    lyrics = fetch_lyrics(url)

    path = url.split("/")[-1]
    lyrics_path = save_lyrics(lyrics, name=path)

    try:
        image_path = download_image("", name=path)
    except:
        image_path = None

    workflow.add_item(
        title="Open lyrics...",
        arg=lyrics_path,
        icon=image_path,
        valid=True,
    )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
