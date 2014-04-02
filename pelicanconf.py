#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
          ('Github', 'http://github.com/griphiam'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATH = 'plugins'
PLUGINS = ['gzip_cache', 'simple_footnotes', 'sitemap', 'tipue_search', 'neighbors', 'extract_toc']

THEME = 'themes/elegant'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)']

TYPOGRIFY = True
RELATED_POSTS_LABEL = 'keep reading...'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'
USE_FAVICON = True

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
		'name': 'iSuperGP',
		'url': 'http://www.isupergp.com',
		'description': 'Mobile front end to <a href="http://supergenpass.com">SupergenPass</a>'
	}
]

LANDING_PAGE_ABOUT = {
	'title': 'Software Engineer, Photographer, Musician',
	'details': '<div><p>So, a little bit about myself...</p></div>'
}

SITESUBTITLE = '"You simian-descended, equivocating, pronoun-starved little mortal twerp" - The Transcendant Pig'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
