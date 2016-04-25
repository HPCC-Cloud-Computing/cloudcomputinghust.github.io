#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Basic details
AUTHOR = u'CloudComputingHust'
SITENAME = u'Cloud Computing Hust'
SITEURL = 'https://cloudcomputinghust.github.io'

# Configuration
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_LANG = u'vi'
DELETE_OUTPUT_DIRECTORY = False
THEME = "Just-Read"
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 50
LOCALE='C'
TAG_CLOUD_STEPS = 8

# URL settings
# We might want this for publication
#RELATIVE_URLS = False
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

# Feeds settings
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/feed.rss'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED = None
TRANSLATION_FEED_ATOM = 'feeds/atom-%s.xml'
TRANSLATION_FEED_RSS = 'feeds/feed-%s.rss'


MENUITEMS =  (('Home', 'http://cloudcomputinghust.github.io'),)


PATH = 'content'
STATIC_PATHS = [
    'extras/favicon.ico',
	'images',
    ]
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
    }
SOCIAL = (('GitHub',  'http://github.com/cloudcomputinghust'),)
# Plugins

#PLUGINS = ["add_translator_line"]
#PLUGIN_PATHS = ["plugins"]
