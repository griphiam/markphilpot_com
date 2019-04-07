#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import logging
import re

log = logging.getLogger(__name__)

def regex_replace(txt, rgx, val, ignorecase=False, multiline=False):
    r'''
    Searches for a pattern and replaces with a sequence of characters.
    .. code-block:: jinja
        {% set my_text = 'lets replace spaces' %}
        {{ my_text | regex_replace('\s+', '__') }}
    will be rendered as:
    .. code-block:: text
        lets__replace__spaces
    '''
    flag = 0
    if ignorecase:
        flag |= re.I
    if multiline:
        flag |= re.M
    compiled_rgx = re.compile(rgx, flag)
    return compiled_rgx.sub(val, txt)


DEBUG = True
SHOW_DRAFTS = True

if DEBUG:
     CACHE_CONTENT = True
     LOAD_CONTENT_CACHE = True
     CHECK_MODIFIED_METHOD = 'mtime'

AUTHOR = 'Mark Philpot'
SITENAME = 'markphilpot.com'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
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
SOCIAL = (('Twitter', 'https://twitter.com/mark_philpot'),
          ('Github', 'https://github.com/markphilpot'),)

DEFAULT_PAGINATION = 10

PATH = 'content'
PLUGIN_PATHS = [
    'plugins', 'plugins_custom',
]

ARTICLE_EXCLUDES = [
    'twitter'
]

# Removed 'gzip_cache' since AWS Cloudfront does it for us
PLUGINS = [
    'frontmark',
    'simple_footnotes', 
    'sitemap', 
    'extract_toc', 
    'neighbors_filtered',
]

# Theme Settings
THEME = 'themes/pelican-theme'
TWITTER_USERNAME='mark_philpot'

#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)', 'markdown.extensions.attr_list']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
        'markdown.extensions.toc': {'anchorlink': True, 'permalink': False}
    },
    'output_format': 'html5',
}
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.loopcontrols']}
JINJA_FILTERS = {'regex_replace': regex_replace}

TYPOGRIFY = False 
RELATED_POSTS_LABEL = 'keep reading...'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
USE_FAVICON = True
WITH_FUTURE_DATES = True
PAGINATED_DIRECT_TEMPLATES = []

# Prevent generation of paginated blocks
AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False

# Prevent category generation during dev
CATEGORY_SAVE_AS = False

STATIC_PATHS = ['theme/images', 'images', 'admin']
STATIC_EXCLUDE_SOURCES = False

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
