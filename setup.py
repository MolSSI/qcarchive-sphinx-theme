import setuptools
import versioneer

short_description = "A sphinx theme for all QCArchive documentation."

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except FileNotFoundError:
    long_description = short_description

if __name__ == "__main__":
    setuptools.setup(
        name='qcarchive-sphinx-theme',
        description=short_description,
        author='Daniel G. A. Smith',
        author_email='dgasmith@vt.edu',
        url="https://github.com/molssi/qcarchive-sphinx-theme",
        license='BSD-3C',
        include_package_data=True,
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=setuptools.find_packages(),
        install_requires=[
            'sphinx_rtd_theme'
        ],
        # http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
        entry_points = {
            'sphinx.html_themes': [
                'qcarchive_sphinx_theme = qcarchive_sphinx_theme',
            ]
        },
        zip_safe=True,
        long_description=long_description,
        long_description_content_type="text/markdown"
    )
