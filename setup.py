# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from sphinxjp.themes.impressjs import __version__

version = __version__

with open("README.rst") as readme_fp:
    readme = readme_fp.read()

with open("AUTHORS.txt") as authoers_fp:
    authors = authoers_fp.read()

with open("HISTORY.txt") as history_fp:
    history = history_fp.read()

long_description = '\n'.join([readme, authors, history])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Framework :: Sphinx',
    'Framework :: Sphinx :: Extension',
    'Framework :: Sphinx :: Theme',
    'Topic :: Documentation',
    'Topic :: Documentation :: Sphinx',
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
    name='sphinxjp.themes.impressjs',
    version=version,
    description='A sphinx theme for HTML presentation style.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme', 'presentation'],
    author='Shoji KUMAGAI',
    author_email='take dot this dot 2 dot your dot grave at gmail dot com',
    url='https://github.com/shkumagai/sphinxjp.themes.impressjs',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'docutils',
        'sphinx',
    ],
    entry_points={
        "sphinx.html_themes": [
            "impressjs = sphinxjp.themes.impressjs",
        ],
    },
    python_requires=">=3.5",
    zip_safe=False,
)
