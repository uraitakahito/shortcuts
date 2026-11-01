# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'shortcuts'
copyright = '2022, Takahito Urai'
author = 'Takahito Urai'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'scrolls'
html_static_path = ['_static']
html_css_files = ['lang-switch.css']

# -- Options for internationalization ----------------------------------------
# Japanese pages are built with -D language=ja (make html-ja). Catalogs live in
# source/locales, Sphinx's default locale_dirs.

gettext_location = False  # keep .po diffs to text changes, not line numbers

from docutils import nodes
from sphinx.transforms import SphinxTransform


class SkipLiteralOnlyTerms(SphinxTransform):
    """Keep key-only terms such as ``⌘ + d`` out of the translation catalogs."""

    default_priority = 10  # before sphinx.transforms.i18n.Locale (20)

    def apply(self, **kwargs):
        for term in self.document.findall(nodes.term):
            if len(term.children) == 1 and isinstance(term[0], nodes.literal):
                term['translatable'] = False


def setup(app):
    app.add_transform(SkipLiteralOnlyTerms)
