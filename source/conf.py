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

extensions = ['myst_parser', 'sphinx_design']
myst_enable_extensions = ['colon_fence']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = 'Keyboard shortcuts for Mac'  # the Japanese build overrides it in the Makefile
html_static_path = ['_static']
html_css_files = ['lang-switch.css']
html_sidebars = {
    '**': [
        'sidebar/scroll-start.html',
        'sidebar/brand.html',
        'sidebar/lang-switch.html',
        'sidebar/search.html',
        'sidebar/navigation.html',
        'sidebar/scroll-end.html',
    ],
}

# -- Options for internationalization ----------------------------------------
# Japanese pages are built with -D language=ja (make html-ja). Catalogs live in
# source/locales, Sphinx's default locale_dirs.

gettext_location = False  # keep .po diffs to text changes, not line numbers

from docutils import nodes
from sphinx.transforms import SphinxTransform


class SkipKeyOnlyText(SphinxTransform):
    """Keep text that is only keys, such as ``⌘ + d`` or {kbd}`⌘+c`, out of the translation catalogs."""

    default_priority = 10  # before sphinx.transforms.i18n.Locale (20)

    def apply(self, **kwargs):
        for node in self.document.findall(lambda n: isinstance(n, (nodes.term, nodes.paragraph))):
            parts = [c for c in node.children if not (isinstance(c, nodes.Text) and not c.strip())]
            if parts and all(isinstance(c, nodes.literal) for c in parts):
                node['translatable'] = False


def setup(app):
    app.add_transform(SkipKeyOnlyText)
