import feedparser
import time


rss = 'https://www.reddit.com/r/Python/.rss'


def notify(title, message):
    import os
    cmd = 'ntfy -t "{0}" send "{1}"'.format(title, message)
    os.system(cmd)


def get_feeds():
    feed = feedparser.parse(rss)
    for key in feed["entries"]: 
        notify(key['title'], key['links'][0]['href'])
        time.sleep(20)


if __name__ == '__main__':
    while True:
        get_feeds()
        time.sleep(90)