# -*- coding: utf-8 -*-

import json
import logging
import os
import re
from argparse import ArgumentParser
import codecs

import errno
from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

log = logging.getLogger('process_twitter_archive')
log.setLevel(logging.INFO)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


# def tweet_to_markdown(tweet):
#     raw = tweet['text'].decode('utf8')
#
#     # Replace @user with [@user](https://twitter.com/user)
#     p = re.compile(r'@(\w+)')
#     markdown = re.sub(p, r'[@\1](https://twitter.com/\1)', raw, 10)
#
#     links = tweet['expanded_urls'].split(',')
#
#     for link in links:
#         markdown = re.sub(r'http[s]?://t.co/[\w\d]+', '[%s](%s)' % (link,link), markdown)
#
#     tweet['markdown'] = markdown
#
#     return tweet


def tweet_to_markdown(tweet):
    is_retweet = False

    if 'retweeted_status' in tweet:
        is_retweet = True
        tweet['retweet_user'] = tweet['retweeted_status']['user']['screen_name']
        raw = tweet['retweeted_status']['text']
        entities = tweet['retweeted_status']['entities']
    else:
        raw = tweet['text']
        entities = tweet['entities']

    # Find all replaceable elements
    replaceable_elements = []
    for url_element in entities['urls']:
        replaceable_elements.append({
            'start': url_element['indices'][0],
            'end': url_element['indices'][1],
            'type': 'url',
            'element': url_element,
        })
    for media_element in entities['media']:
        replaceable_elements.append({
            'start': media_element['indices'][0],
            'end': media_element['indices'][1],
            'type': 'media',
            'element': media_element
        })

    replaceable_elements.sort(key=lambda x: x['start'], reverse=True)

    for rep in replaceable_elements:
        if rep['type'] == 'url':
            raw = raw[0:rep['start']] + u"[{}]({})".format(rep['element']['display_url'], rep['element']['expanded_url']) + raw[rep['end']:]
        elif rep['type'] == 'media':
            #raw = raw[0:rep['start']] + u"\n\n![{}]({}){{: .center}}\n\n".format(rep['element']['display_url'], rep['element']['media_url_https']) + raw[rep['end']:]
            raw = raw[0:rep['start']] + u'\n\n<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="{}" data-src="{}" class="center"/>\n\n'.format(rep['element']['display_url'], rep['element']['media_url_https']) + raw[rep['end']:]

    p = re.compile(r'@(\w+)')
    markdown = re.sub(p, r'[@\1](https://twitter.com/\1)', raw, 10)

    if is_retweet:
        tweet['markdown'] = u'<i class="fa fa-retweet" aria-hidden="true"></i> {}'.format(markdown)
    else:
        tweet['markdown'] = markdown

    return tweet


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    parser = ArgumentParser('Twitter Archive To Markdown Micro')
    parser.add_argument('--output_dir', '-o', default='content/micro')
    parser.add_argument('--input_dir', '-i', help='Path to root of twitter archive')
    parser.add_argument('--overwrite', action='store_true', default=False)

    args = parser.parse_args()

    tweets = []

    JS_PATH = 'data/js/tweets/'

    for js_file in os.listdir('%s/%s' % (args.input_dir, JS_PATH)):
        with codecs.open('%s/%s/%s' % (args.input_dir, JS_PATH, js_file), encoding='utf8') as f:
            lines = f.readlines()
            # Need to drop the first one
            json_string = '\n'.join(lines[1:])
            json_array = json.loads(json_string)
            tweets.extend(json_array)

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    template = env.get_template('micro_blog_post.md')

    for tweet in tweets:
        timestamp = datetime.strptime(tweet['created_at'], "%Y-%m-%d %H:%M:%S +0000")
        year = timestamp.year
        filename = timestamp.strftime("%Y-%m-%dT%H:%M:%S")

        mkdir_p('%s/%d' % (args.output_dir, year))

        tweet['ts'] = timestamp
        tweet['date_field'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        tweet['filename'] = filename
        tweet['tweet_id'] = tweet['id_str']

        tweet = tweet_to_markdown(tweet)

        f_str = '%s/%d/%s.md' % (args.output_dir, year, filename)

        if not os.path.isfile(f_str) or args.overwrite:
            with open(f_str, 'wb') as fp:
                fp.write(template.render(tweet).encode('utf8'))
