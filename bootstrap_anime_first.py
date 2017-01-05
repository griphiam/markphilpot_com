# -*- coding: utf-8 -*-
import logging
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import requests
from jinja2 import FileSystemLoader, Environment
from datetime import datetime
import sys
import errno
import os

from pelicanconf import HUMMINGBIRD_API_KEY

log = logging.getLogger(__name__)

STUDIOS = {
    'a1': {
        'name': 'A1 Pictures',
        'logo': 'images/anime/studios/a1.png'
    },
    'aic': {
        'name': 'Anime International Company',
        'logo': 'images/anime/studios/aic.png'
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

ANILIST_API = 'https://anilist.co/api'

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def anilist_authenticate(client_id, client_secret):
    headers = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    r = requests.post("{}/auth/access_token".format(ANILIST_API), headers=headers)
    r.raise_for_status()
    return r.json()['access_token']


def anilist_browse_season(access_token, year, season, sort='popularity-desc'):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    params = {
        'year': year,
        'season': season,
        'sort': sort,
    }
    r = requests.get("{}/browse/anime", params=params, headers=headers)
    r.raise_for_status()
    return r.json()


def anilist_save_image(anime_model, image_dir=None):
    if image_dir:
        mkdir_p(image_dir)
        filename = anime_model['image_url_lge'].split('/')[-1]
        anime_model['__pv_filename__'] = filename
        img = requests.get(anime_model['image_url_lge'])
        with open('%s/%s' % (image_dir, '%s/%s' % (image_dir, filename)), 'wb') as f:
            f.write(img.content)
            f.close()

    return anime_model


# def parse_hummingbird(slug, image_dir=None):
#     r = requests.get('https://hummingbird.me/api/v2/anime/%s' % slug, headers={'X-Client-Id': HUMMINGBIRD_API_KEY})
#     anime = r.json()['anime']
#
#     if image_dir:
#         mkdir_p(image_dir)
#         filename = anime['poster_image'].split('/')[-1].split('?')[0]
#         anime['pv_filename'] = filename
#         img = requests.get(anime['poster_image'])
#         with open('%s/%s' % (image_dir, '%s/%s' % (image_dir, filename)), 'wb') as f:
#             f.write(img.content)
#             f.close()
#
#     return anime


# def process_hummingbird_upcoming(season, image_dir=None):
#     data = {
#         'shows': [],
#         'season': season
#     }
#     r = requests.get('https://hummingbird.me/anime/upcoming/%s' % season)
#     soup = BeautifulSoup(r.text, 'html5lib')
#
#     entries = soup.find('ul', class_='large-block-grid-5').select('li.card')
#
#     print('Found %d shows' % len(entries))
#
#     if image_dir:
#         mkdir_p(image_dir)
#
#     for e in entries:
#         link = e.find('a')['href']
#         slug = link[7:]
#         try:
#             r = requests.get('https://hummingbird.me/api/v2/anime/%s' % slug,
#                              headers={'X-Client-Id': HUMMINGBIRD_API_KEY})
#             r.raise_for_status()
#             show = r.json()['anime']
#
#             if 'producers' not in show or show['producers'] is None:
#                 show['producers'] = []
#
#             data['shows'].append(show)
#
#             if image_dir:
#                 filename = show['poster_image'].split('/')[-1].split('?')[0]
#                 show['pv_filename'] = filename
#                 img = requests.get(show['poster_image'])
#                 with open('%s/%s' % (image_dir, filename), 'wb') as f:
#                     f.write(img.content)
#                     f.close()
#
#         except Exception, e:
#             log.error(e.message, exc_info=True)
#             print('Skipped %s' % slug)
#             exit(1)
#         sys.stdout.write('.')
#         sys.stdout.flush()
#
#     return data


if __name__ == '__main__':
    """
    Examples:

        python bootstrap_anime_first.py --season spring --year 2017 -o content/2016/anime_spring_first.md --save_images --client_id X --client_secret Y

        mogrify -resize 320x *.jpg # (revert hero.jpg)

    """
    logging.getLogger().addHandler(logging.StreamHandler())

    parser = ArgumentParser('Template bootstrap')
    parser.add_argument('--template', '-t', default=None)
    parser.add_argument('--output', '-o')
    # parser.add_argument('--hummingbird', '-hb', dest='hummingbird_slug')
    # parser.add_argument('--studio', '-s', choices=STUDIOS.keys())
    parser.add_argument('--year')
    parser.add_argument('--season')
    parser.add_argument('--save_images', default=False, action='store_true')
    parser.add_argument('--client_id')
    parser.add_argument('--client_secret')

    args = parser.parse_args()

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    data = {}

    if not args.template and args.season:
        args.template = 'anime_first.md'
    # elif not args.template and args.hummingbird_slug:
    #     args.template = 'anime_review.md'

    dt = datetime.now()
    data['timestamp'] = dt.isoformat(" ")[:-7]
    data['year'] = args.year

    image_dir = None
    if args.season and args.save_images:
        image_dir = 'content/images/anime/%d/%s' % (args.year, args.season)
    # elif args.hummingbird_slug and args.save_images:
    #     image_dir = 'content/images/%d/%s' % (data['year'], args.hummingbird_slug.replace('-', '_'))

    # if args.season and args.season == 'winter':
    #    data['year'] += 1

    # if args.hummingbird_slug:
    #     data.update(parse_hummingbird(args.hummingbird_slug, image_dir))
    # if args.season:
    #     data.update(process_hummingbird_upcoming(args.season, image_dir))

    access_token = anilist_authenticate(args.client_id, args.client_secret)
    anime_models = anilist_browse_season(access_token, args.year, args.season)

    data.update({
        'shows': [anilist_save_image(m, image_dir) for m in anime_models],
        'season': args.season,
    })

    # data['studio'] = STUDIOS.get(args.studio, {'name': 'Unknown', 'logo': 'Unknown'})
    template = env.get_template(args.template)

    if args.output:
        with open(args.output, 'wb') as fp:
            fp.write(template.render(data).encode('utf8'))
    else:
        print(template.render(data))
