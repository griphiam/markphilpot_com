# -*- coding: utf-8 -*-

import csv
import logging
import os
import re
from argparse import ArgumentParser

import errno
from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

log = logging.getLogger('process_twitter_archive')

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def tweet_to_markdown(tweet):
    raw = tweet['text'].decode('utf8')

    # Replace @user with [@user](https://twitter.com/user)
    p = re.compile(r'@(\w+)')
    markdown = re.sub(p, r'[@\1](https://twitter.com/\1)', raw, 10)

    links = tweet['expanded_urls'].split(',')

    for link in links:
        markdown = re.sub(r'http[s]?://t.co/[\w\d]+', '[%s](%s)' % (link,link), markdown)

    tweet['markdown'] = markdown

    return tweet


if __name__ == '__main__':
    logging.getLogger().addHandler(logging.StreamHandler())

    parser = ArgumentParser('Twitter Archive To Markdown Micro')
    parser.add_argument('--output_dir', '-o', default='content/micro')
    parser.add_argument('--input', '-i', help='Twitter archive csv')
    parser.add_argument('--overwrite', action='store_true', default=False)

    args = parser.parse_args()

    tweets = []

    with open(args.input) as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = csv_reader.next()

        for row in csv_reader:
            tweets.append(dict(zip(fields, row)))

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    template = env.get_template('micro_blog_post.md')

    for tweet in tweets:
        timestamp = datetime.strptime(tweet['timestamp'], "%Y-%m-%d %H:%M:%S +0000")
        year = timestamp.year
        filename = timestamp.strftime("%Y-%m-%dT%H:%M:%S")

        mkdir_p('%s/%d' % (args.output_dir, year))

        tweet['ts'] = timestamp
        tweet['filename'] = filename

        tweet = tweet_to_markdown(tweet)

        f_str = '%s/%d/%s.md' % (args.output_dir, year, filename)

        if not os.path.isfile(f_str) or args.overwrite:
            with open(f_str, 'wb') as fp:
                fp.write(template.render(tweet).encode('utf8'))
