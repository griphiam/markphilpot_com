#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging

log = logging.getLogger(__name__)

DEBUG = True

AUTHOR = u'Mark Philpot'
SITENAME = u'markphilpot.com'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

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
PLUGINS = ['gzip_cache', 'simple_footnotes', 'sitemap', 'tipue_search', 'neighbors', 'extract_toc']

THEME = 'themes/elegant'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)', 'markdown.extensions.attr_list']

TYPOGRIFY = True
RELATED_POSTS_LABEL = 'keep reading...'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = u'pages/{slug}/'
PAGE_SAVE_AS = u'pages/{slug}/index.html'
USE_FAVICON = True
WITH_FUTURE_DATES = True

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

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

PROJECTS = [
    {
        'name': 'DaedaFusion OSS',
        'url': 'https://github.com/daedafusion',
        'description': 'Plugable component architecture'
    },
    {
        'name': 'TriAxis Editor',
        'url': 'http://triaxiseditor.com',
        'description': 'Web config editor for the Mesa Boogie TriAxis'
    },
    {
        'name': 'GCP Editor',
        'url': 'http://gcproeditor.com',
        'description': 'Web config editor for the Voodoo Labs GCP'
    },
	{
		'name': 'iSuperGP',
		'url': 'http://www.isupergp.com',
		'description': 'Mobile front end to <a href="http://supergenpass.com">SupergenPass</a>'
	}
]

LANDING_PAGE_ABOUT = {
	'title': 'Software Engineer, Photographer, Musician',
	'details': """
        <div>
            <p>So, a little bit about myself...</p>
            <p>Software :: how I currently make my living.  I'm a full stack engineer -- so everything from databases, backend services and through to the user interface is fair game.</p>
            <p>Photos &amp; Music :: hobbies, outlets, just fun.</p>
        </div>
    """
}

SITESUBTITLE = '"You simian-descended, equivocating, pronoun-starved little mortal twerp" - The Transcendant Pig'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INCLUDE_HUMMINGBIRD_CURRENTLY_WATCHING = True
HUMMINGBIRD_USERNAME = 'mphilpot'
HUMMINGBIRD_API_KEY = '0084bb364f1201c86837'

if INCLUDE_HUMMINGBIRD_CURRENTLY_WATCHING:
    import requests

    r = requests.get('https://hummingbird.me/api/v1/users/%s/library?status=currently-watching' % HUMMINGBIRD_USERNAME)
    try:
        r.raise_for_status()
        shows = r.json()
        covers = map(lambda x: ( x['anime']['cover_image'], x['anime']['url'] ), shows)

        log.info('Found %d covers' % len(covers))

        img_template = """<a href="%s"><img src="%s" width=75 title="%s"/></a>"""
        wrapper_template = """
            <div>
                <h3>Currently Watching</h3>
                <p>%s</p>
            </div>
        """

        LANDING_PAGE_ABOUT['details'] += wrapper_template % "".join(
            map(lambda x: img_template % (x['anime']['url'],
                                          x['anime']['cover_image'],
                                          x['anime']['title']), shows)
        )

    except Exception as e:
        log.error('Error processing currently watched', exc_info=True)
