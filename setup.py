# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


from sphinxjp.themes.impressjs import __version__


version = __version__
long_description = '\n'.join([
    open(os.path.join("src", "README.txt")).read(),
    open(os.path.join("src", "AUTHORS.txt")).read(),
    open(os.path.join("src", "HISTORY.txt")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
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
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['buildout.cfg']},
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
    zip_safe=False,
)
