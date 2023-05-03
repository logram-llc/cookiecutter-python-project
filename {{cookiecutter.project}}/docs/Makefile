# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXAPIDOC   =  sphinx-apidoc
SPHINXBUILD   ?= sphinx-build
SOURCE_DIR     =  source
BUILD_DIR      =  build
HTML_DIR       = $(BUILD_DIR)/html
PACKAGE_DIR    =  ../{{ cookiecutter.slug }}

PROJECT_NAME        = {{ cookiecutter.project }}
VERSIONS_DIR        =  versions
VERSION            := $(shell python ./get_version.py)
VERSIONED_BUILD_DIR = "$(VERSIONS_DIR)"/"$(VERSION)"
LATEST_BUILD_DIR    = "$(VERSIONS_DIR)"/latest

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCE_DIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXAPIDOC) -o "$(SOURCE_DIR)" "$(PACKAGE_DIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCE_DIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)

	$(shell python ./simplify-module-titles.py)

	mkdir -p "$(VERSIONS_DIR)"
	rm -rf "$(VERSIONED_BUILD_DIR)" "$(LATEST_BUILD_DIR)"
	cp -r "$(HTML_DIR)" "$(VERSIONED_BUILD_DIR)"
	cp -r "$(HTML_DIR)" "$(LATEST_BUILD_DIR)"
	rm -r "$(BUILD_DIR)"
