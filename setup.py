import os

from setuptools import setup, find_packages


# XXX: these should go into the package's __init__
VERSION = '0.1.0'
AUTHOR = 'FND'
LICENSE = 'BSD'

DESC = os.path.join(os.path.dirname(__file__), 'README')

META = {
    'name': 'tiddlywebplugins.rdf',
    'url': 'https://github.com/FND/tiddlywebplugins.rdf',
    'version': VERSION,
    'description': 'TiddlyWeb RDF serializer',
    'long_description': DESC,
    'license': LICENSE,
    'author': AUTHOR,
    'packages': find_packages(exclude=['test']),
    'platforms': 'Posix; MacOS X; Windows',
    'include_package_data': False,
    'zip_safe': False,
    'install_requires': ['tiddlyweb'],
    'extras_require': {
        'testing': ['pytest'],
        'coverage': ['figleaf', 'coverage']
    }
}


if __name__ == '__main__':
    setup(**META)
