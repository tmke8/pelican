AUTHOR = "Lemony Snicket"
SITENAME = "Minimal blog"
SITEURL = ""
THEME = "./theme"

SLUGIFY_SOURCE = "basename"
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"
TAGS_SAVE_AS = "tags/index.html"

MENUITEMS = [("Home", "./"), ("Categories", "categories/")]
DEFAULT_CATEGORY = "Uncategorized"
PATH = "content"
DISPLAY_PAGES_ON_MENU = True

TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Pelican", "https://getpelican.com/"),
         ("Python.org", "https://www.python.org/"),
         ("Jinja2", "https://palletsprojects.com/p/jinja/"),
         ("You can modify those links in your config file", "#"),)

# Social widget
SOCIAL = (("You can add links in your config file", "#"),
          ("Another social link", "#"),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
