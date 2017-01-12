#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import logging

log = logging.getLogger(__name__)

DEBUG = True

if DEBUG:
     CACHE_CONTENT = True
     LOAD_CONTENT_CACHE = True
     CHECK_MODIFIED_METHOD = 'mtime'

AUTHOR = u'Mark Philpot'
SITENAME = u'markphilpot.com'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %-d, %Y')
NOW = datetime.datetime.now()

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/mark_philpot'),
          ('Github', 'http://github.com/markphilpot'),)

DEFAULT_PAGINATION = 10

PATH = 'content'
PLUGIN_PATHS = [
    'plugins',
]

# Removed 'gzip_cache' since AWS Cloudfront does it for us
PLUGINS = ['simple_footnotes', 'sitemap', 'neighbors', 'extract_toc']

# Theme Settings
THEME = 'themes/pelican-theme'
TWITTER_USERNAME='mark_philpot'

#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)', 'markdown.extensions.attr_list']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
        'markdown.extensions.toc': {'permalink': 'true'}
    },
    'output_format': 'html5',
}

TYPOGRIFY = True
RELATED_POSTS_LABEL = 'keep reading...'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = u'pages/{slug}/'
PAGE_SAVE_AS = u'pages/{slug}/index.html'
USE_FAVICON = True
WITH_FUTURE_DATES = True
PAGINATED_DIRECT_TEMPLATES = []

# Prevent generation of paginated blocks
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False

STATIC_PATHS = ['theme/images', 'images']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

#DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
DIRECT_TEMPLATES = (('index', 'micro'))

SITESUBTITLE = '"You simian-descended, equivocating, pronoun-starved little mortal twerp" - The Transcendant Pig'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True