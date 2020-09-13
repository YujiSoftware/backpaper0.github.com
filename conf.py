# -*- coding: utf-8 -*-

import tinkerer
import tinkerer.paths        

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = u'裏紙'                   

# Change this to the tagline of your blog
tagline = u'I ❤️ BotW.'

# Change this to your name
author = u'うらがみ'

# Change this to your copyright string
copyright = u'2013-2020, ' + author         

# Change this to your blog root URL (required for RSS feed)
website = 'https://backpaper0.github.io/'                              

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = None                                   

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'backpaper0.ico'           

# Pick another Tinkerer theme or use your own
html_theme = "tinkerbelizehole"

# Theme-specific options, see docs
html_theme_options = { }                                  

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Number of blog posts per page
posts_per_page = 2

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus', 'sphinxjp.themecore'] 

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]                 

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*"]                                     

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["recent.html", "searchbox.html"]
}

# **************************************************************
# Do not modify below lines as the values are required by 
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
