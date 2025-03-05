# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme
import os
print("XeLaTeX path:", os.popen("which xelatex").read().strip())
print("Latexmk path:", os.popen("which latexmk").read().strip())

# -- Project information
project = 'Feature Engineering in Machine Learning'
copyright = '2025, Bình Phạm'
author = 'Bình Phạm'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'nbsphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_gallery.load_style',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

templates_path = ['_templates']

# -- Options for HTML output
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
highlight_language = 'python3'
epub_show_urls = 'footnote'

# Set the language to Vietnamese
language = 'vi'

# -- Options for LaTeX output
latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}
''',
    'babel': '',
    'polyglossia': r'''
\usepackage{polyglossia}
\setdefaultlanguage{vietnamese}
\setotherlanguage{english}
\newfontfamily\vnfont{Times New Roman}
\newcommand{\textvn}[1]{{\vnfont #1}}
''',
    'preamble': r'''
\usepackage{titlesec}
\titleformat{\chapter}[hang]{\Large\bfseries}{\thechapter}{1em}{}
\usepackage{microtype}
\renewcommand{\baselinestretch}{1.2}
\XeTeXlinebreaklocale "vn"
\XeTeXlinebreakskip = 0pt plus 1pt
''',
}
