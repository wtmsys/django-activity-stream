# -*- coding: utf-8 -*-
#
# Django Activity Stream documentation build configuration file, created by
# sphinx-quickstart on Sat Oct  1 12:35:29 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import os
import sys
from datetime import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'runtests.settings'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../runtests'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def init():
    import django
    try:
        django.setup()
    except AttributeError:
        pass
    import actstream
    return actstream


actstream = init()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Django Activity Stream'
copyright = 'Django Activity Stream 2010-%s by Justin Quick. <br/> Activity Streams logo released under <a href="http://creativecommons.org/licenses/by/3.0/">Creative Commons 3.0</a>' % datetime.now().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = actstream.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'tango'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'logo.jpg',
    'logo_text_align': 'center',
    'github_user': 'justquick',
    'github_repo': 'django-activity-stream',
    'github_banner': 'img/fork.png',
    'github_button': True,
    'github_type': 'star',
    'description': 'Generate generic activity streams from the actions on your site. Users can follow any actors activities for personalized streams',
    'page_width': '1000px',
    'analytics_id': 'UA-42089198-1'
}
html_static_path = ['_static']
html_css_files = ['style.css']

# Output file base name for HTML help builder.
htmlhelp_basename = 'DjangoActivityStreamdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'DjangoActivityStream.tex', 'Django Activity Stream Documentation',
   'Justin Quick', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'djangoactivitystream', 'Django Activity Stream Documentation',
     ['Justin Quick'], 1)
]
