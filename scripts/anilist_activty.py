# -*- coding: utf-8 -*-
import logging
from argparse import ArgumentParser

import datetime
import requests
from jinja2 import FileSystemLoader, Environment

import os
import errno

log = logging.getLogger(__name__)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


activityQuery = """
query userActivity($userId: Int, $page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage){
    activities(userId: $userId, sort: ID_DESC) {
      __typename
      ... on ListActivity {
        id
        type
        status
        progress
        createdAt
        media {
          type
          title {
            romaji
          }
          coverImage {
            medium
          }
        }
      }
    }
    pageInfo {
      total
      currentPage
      hasNextPage
    }
  }
}
"""

def get_activity(userId):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    page = 0
    payload = {
        'query': activityQuery,
        'variables': {
            'userId': userId,
            'page': page,
            'perPage': 100
        }
    }

    activity = []

    r = requests.post('https://graphql.anilist.co', json=payload, headers=headers).json()

    while r['data']['Page']['pageInfo']['hasNextPage']:
        log.info('Loaded page {}'.format(page))
        activity.extend(r['data']['Page']['activities'])
        page = page+1
        payload['variables']['page'] = page
        r = requests.post('https://graphql.anilist.co/', json=payload, headers=headers).json()

    log.info('Found {} activities'.format(len(activity)))

    return activity


def bucket_activity(activity):
    activity_buckets = {}

    for a in activity:
        try:
            ts = datetime.datetime.fromtimestamp(a['createdAt'])
            key = ts.strftime("%Y-%m-%d")

            if key not in activity_buckets:
                activity_buckets[key] = []

            activity_buckets[key].append(a)
        except:
            log.error(a)

    return activity_buckets


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    parser = ArgumentParser('Anilist Activity')
    parser.add_argument('--template', '-t', default='anilist_activity.md')
    parser.add_argument('--output', '-o', default='content/anilist_activity')

    parser.add_argument('--user_id', type=int, default=85236)
    parser.add_argument('--save_images', default=False, action='store_true')
    parser.add_argument('--overwrite', action='store_true', default=False)

    args = parser.parse_args()

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    template = env.get_template(args.template)

    log.info('Fetching activity...')
    activity = get_activity(args.user_id)

    buckets = bucket_activity(activity)

    log.info('Found activity on {} days'.format(len(buckets.keys())))

    for k, v in buckets.items():
        ts = datetime.datetime.strptime(k, "%Y-%m-%d")
        year = ts.year

        payload = {
            'ts': ts,
            'key': k,
            'date_field': ts.strftime("%Y-%m-%d %H:%M:%S"),
            'activity': v
        }

        mkdir_p('%s/%d' % (args.output, year))

        f_str = '%s/%d/%s.md' % (args.output, year, k)

        if not os.path.isfile(f_str) or args.overwrite:
            with open(f_str, 'wb') as fp:
                fp.write(template.render(payload).encode('utf8'))