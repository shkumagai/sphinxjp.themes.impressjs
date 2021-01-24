# -*- coding: utf-8 -*-

from os import path

from . import directives


VERSION = (0, 5, 0)

__version__ = ".".join(str(n) for n in VERSION)


package_dir = path.abspath(path.dirname(__file__))


def get_path():
    """entry-point for sphinxjp.themecore theme."""
    return path.join(package_dir, 'templates', 'impressjs')


def setup(app):
    """entry-point for sphinxjp.themecore directives."""
    app.add_html_theme('impressjs', get_path())

    directives.setup(app)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
