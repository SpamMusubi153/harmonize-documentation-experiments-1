# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Harmonize'
copyright = '2025, -'
author = '-'

# Add ability to import code, if code isn't installable.
# import sync_dispatch
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
sys.path.insert(0, "../../harmonize")

extensions = [
    "sphinx.ext.duration",

    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "breathe",
    
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

breathe_projects = {"Harmonize cpp": "./xml/"}
breathe_default_project = "Harmonize cpp"




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
