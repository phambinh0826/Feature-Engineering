# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme

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
    'rst2pdf.pdfbuilder',  # Thêm phần mở rộng này để hỗ trợ xuất PDF
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Add any paths that contain templates here, relative to this directory.
# The template links to a custom style css to increase the width of displayed content
templates_path = ['_templates']

# -- Options for HTML output
html_static_path = ['_static']

# -- The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

highlight_language = 'python3'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Set the language to Vietnamese
language = 'vi'

# -- Options for PDF output
pdf_documents = [('index', 'FeatureEngineering', 'Feature Engineering in Machine Learning', 'Bình Phạm')]
pdf_language = "vi"
pdf_fit_mode = "shrink"
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
pdf_break_level = 1
pdf_verbosity = 0
pdf_use_index = True
pdf_use_modindex = True
pdf_use_coverpage = True
pdf_cover_template = 'sphinxcover.tmpl'
pdf_default_dpi = 72

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
'''
}

latex_elements = {
    'babel': '\\usepackage[vietnamese]{babel}',
}
