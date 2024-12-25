# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import time

# -- Project information -----------------------------------------------------

project = 'SunFounder Thales Kit for Raspberry Pi Pico'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_rtd_theme',
]

# -- sphinx_rtd_theme Theme options -----------------------------------------------------
html_theme_options = {
    'flyout_display': 'attached'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#from recommonmark.parser import CommonMarkParser
#source_parsers = {
#    '.md': CommonMarkParser,
#}
#source_suffix = ['.rst', '.md']

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

# open link in a new window

rst_epilog = """

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>

.. |link_micropython| raw:: html

    <a href="https://en.wikipedia.org/wiki/MicroPython" target="_blank">MicroPython - Wikipedia</a>
    
.. |link_thonny| raw:: html

    <a href="https://thonny.org/" target="_blank">Thonny</a>

.. |link_sunfounder_controller| raw:: html

    <a href="https://docs.sunfounder.com/projects/sf-controller/en/latest/" target="_blank">SunFounder Control</a>

.. |link_realpython| raw:: html

    <a href="https://realpython.com/micropython/" target="_blank">realpython</a>

.. |link_micropython_pi| raw:: html

    <a href="https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython" target="_blank">method</a>

.. |link_Thales_kit| raw:: html

    <a href="https://www.sunfounder.com/products/pico-starter-kit?_pos=1&_sid=f4bc507fe&_ss=r" target="_blank">Thales Starter Kit</a>

.. |link_Thale_kit| raw:: html

    <a href="https://www.sunfounder.com/products/pico-starter-kit?_pos=1&_sid=f4bc507fe&_ss=r" target="_blank">Purchase Link for Thales Kit</a>


"""
