try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Exercise 43',
    'author': '',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex43'],
    'scripts': [],
    'name': 'projectname'

}

setup(**config)
