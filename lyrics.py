# coding=utf-8

import sys

from workflow import Workflow

from scraper import fetch_lyrics
from utils import load_image, load_lyrics, save_lyrics


def main(workflow):
    url = workflow.args[0]
    path = url.split("/")[-1]

    image_path = load_image(path)
    lyrics_path = load_lyrics(path)

    if not lyrics_path:
        lyrics_path = save_lyrics(fetch_lyrics(url), path)

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
