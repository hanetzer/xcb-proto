# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'xcbgen',
    version = '1.13',
    url = 'https://xcb.freedesktop.org',
    package_dir = {'': 'lib'},
    packages = ['xcbgen'],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development'
    ]
)
