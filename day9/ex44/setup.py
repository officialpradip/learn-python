from flask import Config


try:
    from setuptools import setup
except ImportError:  # ImportError EXIST WHWN PYTHON PROGRAM TRIES TO IMPORT THE MODEL THAT DOESN'T EXIST
    from distutils.core import setup

config = {
    'description': 'Advance User Input',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex44'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
