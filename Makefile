# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# -- Translation ---------------------------------------------------------------
# po:      extract messages and update source/locales/ja/LC_MESSAGES/*.po
# html-ja: build the Japanese pages into build/html/ja (own doctree cache)
# site:    build both languages, as the Pages workflow does
.PHONY: po html-ja site
po:
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@sphinx-intl update -p "$(BUILDDIR)/gettext" -l ja -d "$(SOURCEDIR)/locales"

html-ja:
	@$(SPHINXBUILD) -b html -D language=ja -D html_title="Mac のキーボードショートカット" -d "$(BUILDDIR)/doctrees-ja" "$(SOURCEDIR)" "$(BUILDDIR)/html/ja" $(SPHINXOPTS) $(O)

site: html html-ja
