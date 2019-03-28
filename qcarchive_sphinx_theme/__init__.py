from os import path

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cwd = path.abspath(path.dirname(path.dirname(__file__)))
    return cwd

# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('qcarchive_sphinx_theme', path.abspath(path.dirname(__file__)))
#    app.add_stylesheet('https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css')
#    app.add_stylesheet('https://qcarchive.molssi.org/scss/style.min.d8e1cc812e5417b81797fc88920a0932c6ce7e1e65cde639b11f5401b8ff4db7.css')
#    app.add_stylesheet('https://qcarchive.molssi.org/plugins/themefisher-font/style.css')


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
