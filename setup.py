from setuptools import setup, find_packages
setup(
    name = "artisan",
    version = "0.0.1",
    packages = find_packages(),
    scripts = [],

    install_requires = [
        "python-faker >= 0.2.4",
    ],

    package_data = {
        'src/artisan': ['*.py'],
    },

    # metadata for upload to PyPI
    author = "Kristofer M White",
    author_email = "me@kmwhite.net",
    description = "A python testing library to help craft better tests",
    license = "BSD",
    keywords = "tdd testing unit unittest",
    url = "http://github.com/kmwhite/artisan/",
)
