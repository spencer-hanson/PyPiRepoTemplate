# Test imports for this script before running it
import wheel
import twine
import sphinx
import sphinx_rtd_theme

build_docs_script = None
setup_py = None
sphinx_conf_py = None
sphinx_modules_rst = None
sphinx_installation_rst = None


# source_name
files_to_generate = {
    "build_docs_script.py": build_docs_script,
    "setup.py": setup_py,
    "docs/source/conf.py": sphinx_conf_py,
    "docs/source/modules.rst": sphinx_modules_rst
    "docs/source/main/installation.rst": sphinx_installation_rst
}

# TODO create source folder, generate files above, work on todo list in readme

sphinx_installation_rst = """Installation
============


Install with the pip package on pypi by using the command

.. code-block:: bash

    pip install {{source_name}}

"""


sphinx_modules_rst = """{{source_name}}
==========

.. toctree::
   :maxdepth: 4

   {{source_name}}

"""


sphinx_conf_py = """# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{{source_name}}'
copyright = 'Spencer Hanson'
author = 'Spencer Hanson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


def skip(app, what, name, obj, would_skip, options):  # Don't skip the __init__ methods docstrings
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
"""


setup_py = """from setuptools import setup, find_packages

VERSION = "0.0.1"


def parse_requirements(requirement_file):
    with open(requirement_file) as fi:
        return fi.readlines()


with open('./README.rst') as f:
    long_description = f.read()


setup(
    name='{{source_name}}',
    packages=find_packages(),
    version=VERSION,
    description='TODO edit me',
    author='Spencer Hanson',
    long_description=long_description,
    install_requires=parse_requirements('requirements.txt'),
    keywords=[],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)

"""

build_docs_script = """import os
import subprocess


def main():
    os.chdir("docs")

    subprocess.run(["make.bat", "clean"])

    print("Generating API docs..")
    subprocess.run(["sphinx-apidoc", "-o", "source",  "../{{source_name}}", "-f"])

    print("Generating HTML docs..")

    subprocess.run(["sphinx-build",  "-b", "html", "source", "build"])

    print("Making HTML docs..")
    # TODO Might need a different command on Linux/Mac, try uncommenting below line and commenting
    #  out the 'make.bat' line

    # subprocess.run(["make", "html"])
    subprocess.run(["make.bat", "html"])

    print("Done!")


if __name__ == "__main__":
    main()
"""
