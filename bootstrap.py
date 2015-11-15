# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
from jinja2 import FileSystemLoader, Environment
from datetime import datetime
import sys

from pelicanconf import HUMMINGBIRD_API_KEY

STUDIOS = {
    'a1': {
        'name': 'A1 Pictures',
        'logo': 'images/anime/studios/a1.png'
    },
    'bones': {
        'name': 'Bones',
        'logo': 'images/anime/studios/bones.png'
    },
    'brains': {
        'name': 'Brains Base',
        'logo': 'images/anime/studios/brains_base.png'
    },
    'jc': {
        'name': 'JC Staff',
        'logo': 'images/anime/studios/jc_staff.png'
    },
    'kyoto': {
        'name': 'Kyoto Animation',
        'logo': 'images/anime/studios/kyoto.png'
    },
    'lerche': {
        'name': 'Lerche',
        'logo': 'images/anime/studios/lerche.png'
    },
    'madouse': {
        'name': 'Madhouse',
        'logo': 'images/anime/studios/madhouse.png'
    },
    'pa': {
        'name': 'PA Works',
        'logo': 'images/anime/studios/pa_works.png'
    },
    'ig': {
        'name': 'Production IG',
        'logo': 'images/anime/studios/production_ig.png'
    },
    'shaft': {
        'name': 'Shaft',
        'logo': 'images/anime/studios/shaft.png'
    },
    'tbs': {
        'name': 'TBS',
        'logo': 'images/anime/studios/tbs.png'
    },
    'trigger': {
        'name': 'Trigger',
        'logo': 'images/anime/studios/trigger.png'
    },
    'troyca': {
        'name': 'Troyca',
        'logo': 'images/anime/studios/troyca.png'
    },
    'ufotable': {
        'name': 'Ufotable',
        'logo': 'images/anime/studios/ufotable.png'
    },
    'whitefox': {
        'name': 'WhiteFox',
        'logo': 'images/anime/studios/white_fox.png'
    },
    'wit': {
        'name': 'WIT',
        'logo': 'images/anime/studios/wit.png'
    }
}

def parse_hummingbird(slug):
    r = requests.get('https://hummingbird.me/api/v2/anime/%s' % slug, headers={'X-Client-Id': HUMMINGBIRD_API_KEY})
    return r.json()['anime']

def process_hummingbird_upcoming(season, get_studio=False):
    data = {
        'shows': [],
        'season': season
    }
    r = requests.get('https://hummingbird.me/anime/upcoming/%s' % season)
    soup = BeautifulSoup(r.text, 'html5lib')

    entries = soup.find('ul', class_='large-block-grid-5').select('li.card')

    print('Found %d shows' % len(entries))

    for e in entries:
        link = e.find('a')['href']
        slug = link[7:]
        try:
            r = requests.get('https://hummingbird.me/api/v2/anime/%s' % slug, headers={'X-Client-Id': HUMMINGBIRD_API_KEY})
            r.raise_for_status()
            show = r.json()['anime']

            if 'producers' not in show or show['producers'] is None:
                show['producers'] = []

            data['shows'].append(show)

            if get_studio:
                r = requests.get('https://hummingbird.me/anime/')

        except:
            print('Skipped %s' % slug)
        sys.stdout.write('.')
        sys.stdout.flush()

    return data

# def parse_animutank_preview(url):
#     response = {
#         'shows': []
#     }
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html5lib')
#
#     entries = soup.select('h1.main-title')
#
#     for e in entries:
#         show = {
#             'titles': {
#                 'canonical': e.get('data-romaji', 'unknown'),
#                 'english': e.get('data-english', 'unknown')
#             }
#         }
#
#         siblings = e.find_next_siblings('p')
#         studio_sibling = siblings[1]
#         studio_el = studio_sibling.find('a')
#         show['studio'] = studio_el.string if studio_el else 'uknown'
#
#         if len(siblings) > 5:
#             pv_sibling = siblings[5]
#             pv_el = pv_sibling.find('a')
#             show['pv'] = pv_el['href'] if pv_el else 'unknown'
#
#         response['shows'].append(show)
#
#     return response

if __name__ == '__main__':
    parser = ArgumentParser('Template bootstrap')
    parser.add_argument('--template', '-t')
    parser.add_argument('--output', '-o')
    parser.add_argument('--hummingbird', '-hb', dest='hummingbird_slug')
    parser.add_argument('--studio', '-s', choices=STUDIOS.keys())
    parser.add_argument('--season')

    args = parser.parse_args()

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    data = {}

    if args.hummingbird_slug:
        data.update(parse_hummingbird(args.hummingbird_slug))
    if args.studio:
        data['studio'] = STUDIOS.get(args.studio, {'name': 'Unknown', 'logo': 'Unknown'})
    if args.season:
        data.update(process_hummingbird_upcoming(args.season))

    template = env.get_template(args.template)

    dt = datetime.now()
    data['timestamp'] = dt.isoformat(" ")[:-7]
    data['year'] = int(data['timestamp'][:4])

    if args.season and args.season == 'winter':
        data['year'] += 1

    if args.output:
        with open(args.output, 'wb') as fp:
            fp.write(template.render(data).encode('utf8'))
    else:
        print(template.render(data))
