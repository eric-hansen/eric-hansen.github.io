#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DIRECT_TEMPLATES = ("index", "authors", "tags", "categories", "archives", "search")

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['post_stats', 'pelican-toc', 'tipue_search']

USE_TIPUE_SEARCH = True

TYPOGRIFY = True

AUTHOR = 'Eric Hansen'
AUTHOR_EMAIL = 'hansen.c.eric@gmail.com'
SITENAME = "Eric Hansen's Blog of Stuff"
SITEURL = ''
SITELOGO = 'https://en.gravatar.com/userimage/184664409/2278f2b94cafeb6089594b6ec3c2d0a6.jpg?size=200'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SLUGIFY_USE_UNICODE = True

# Blogroll
LINKS = (
#         ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),
        )

# Social widget
SOCIAL = (
          ('github', 'https://github.com/eric-hansen'),
          ('linkedin', 'https://www.linkedin.com/in/ericchansen/'),
         )

MENUITEMS = (
  ("Archives", "/archives.html"),
  ("Categories", "/categories.html"),
  ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./themes/Flex"
THEME_COLOR = 'dark'
PYGMENTS_STYLE_DARK = 'monokai'

MAIN_MENU = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

COPYRIGHT_YEAR = 2020
