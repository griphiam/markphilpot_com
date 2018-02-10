# -*- coding: utf-8 -*-
import logging
from argparse import ArgumentParser
import requests
from jinja2 import FileSystemLoader, Environment

log = logging.getLogger(__name__)

activityQuery = """
query userActivity($userId: Int, $page: Int) {
  Page(page: $page, perPage: 100){
    activities(userId: $userId, sort: ID_DESC) {
      __typename
      ... on ListActivity {
        id
        type
        status
        media {
          title {
            romaji
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


if __name__ == '__main__':
    logging.getLogger().addHandler(logging.StreamHandler())

    parser = ArgumentParser('Anilist Activity')
    parser.add_argument('--template', '-t', default='anilist_activity.md')
    parser.add_argument('--output', '-o', default='content/anilist_activity')

    parser.add_argument('--userId', type=int, default=85236)
    parser.add_argument('--save_images', default=False, action='store_true')

    args = parser.parse_args()

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    data = {}