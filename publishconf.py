#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://jamesaddison.ca'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_DOMAIN = SITEURL
AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "jamesaddison"
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-69700-6'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'

OUTPUT_PATH = '../jaddison.github.io'
