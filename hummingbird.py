import argparse
import logging

import requests
from jinja2 import FileSystemLoader, Environment

log = logging.getLogger(__name__)

HUMMINGBIRD_USERNAME = 'mphilpot'

def anime():
    data = {
        'anime': {
            'watching': None,
            'completed': None
        },
        'manga': {
            'reading': None,
            'completed': None
        }
    }
    r = requests.get('https://hummingbird.me/api/v1/users/%s/library?status=currently-watching' % HUMMINGBIRD_USERNAME)
    r.raise_for_status()
    shows = r.json()
    covers = map(lambda x: ( x['anime']['cover_image'], x['anime']['url'], x['anime']['title'] ), shows)

    log.info('Found %d watching covers' % len(covers))

    data['anime']['watching'] = covers

    r = requests.get('https://hummingbird.me/api/v1/users/%s/library?status=completed' % HUMMINGBIRD_USERNAME)
    r.raise_for_status()
    shows = r.json()
    covers = map(lambda x: ( x['anime']['cover_image'], x['anime']['url'], x['anime']['title'] ), shows)

    log.info('Found %d completed covers' % len(covers))

    data['anime']['completed'] = covers

    return data

def manga():
    return {}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hummingbird Content Renderer')

    parser.add_argument('--am', default=False, action='store_true', help='Render Anime & Manga Page')
    parser.add_argument('--output', '-o')

    args = parser.parse_args()

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    data = {}

    if args.am:
        data.update(anime())
        data.update(manga())
        template = env.get_template('anime_manga_page.md')

    if args.output:
        with open(args.output, 'wb') as fp:
            fp.write(template.render(data).encode('utf8'))
    else:
        print(template.render(data))