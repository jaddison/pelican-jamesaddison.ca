#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEFAULT_LANG = u'en'
TIMEZONE = 'America/Vancouver'

AUTHOR = u'James Addison'
SITENAME = u'James Addison'
SITEURL = 'http://jamesaddison.ca'

PATH = 'content'
OUTPUT_RETENTION = ('.git', 'CNAME')

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 20

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'

DIRECT_TEMPLATES = ('index', 'archives')

THEME = 'theme'
TYPOGRIFY = True

HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False

USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_USERNAME = 'jamesaddison'
SOCIAL = (
    ('Twitter', 'https://twitter.com/jamesaddison'),
    ('LinkedIn', 'https://www.linkedin.com/in/jamesaddison'),
    ('Github', 'https://github.com/jaddison/'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
