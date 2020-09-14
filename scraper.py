# coding=utf-8

import time

from workflow import web

from BeautifulSoup import BeautifulSoup, NavigableString


def parse(tag):
    if isinstance(tag, NavigableString):
        return [str(tag).strip()]

    lines = []

    for item in tag.contents:
        lines += parse(item)

    return lines


def _fetch(url):
    content = web.get(url)
    soup = BeautifulSoup(content.text)

    return parse(soup.find(u"div", {u"class": u"lyrics"}).find(u"p"))


def fetch_lyrics(url, attemps=5):
    if attemps == 0:
        return None

    try:
        return _fetch(url)
    except:
        time.sleep(0.1)
        return fetch_lyrics(url, attemps=attemps - 1)
