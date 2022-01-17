# Configuration file for the Sphinx documentation builder.
from datetime import datetime

now = datetime.now()

# -- Project information

project = 'GLYN CMS Manual'
copyright = '{}, Matchstick 256 Studio Limited'.format(now.year)
author = 'Matchstick 256 Studio'

version = "{}.{}.{}".format(*now.isocalendar())
# The full version, including alpha/beta/rc tags.
release = "{}.{}.{}".format(*now.isocalendar())

exclude_patterns = ["_build"]

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
