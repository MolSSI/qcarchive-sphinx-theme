from os import path

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cwd = path.abspath(path.dirname(path.dirname(__file__)))
    return cwd

# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_stylesheet("css/small-apps.css")
    app.add_stylesheet("css/themefisher-font.css")
    app.add_html_theme('qcarchive_sphinx_theme', path.abspath(path.dirname(__file__)))


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
