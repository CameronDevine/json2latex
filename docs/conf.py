import os, sys

sys.path.insert(0, os.path.abspath(".."))

project = "json2latex"
copyright = "2020, Cameron Devine"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
autoclass_content = "both"
master_doc = "index"
