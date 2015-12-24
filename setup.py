
from setuptools import setup

version = '0.1'

setup(
    name = 'oandapy',
    version = version,
    description = "Python wrapper for OANDA's REST API",
    long_description = "",
    url = 'http://developer.oanda.com/',
    author = 'OANDA',
    author_email = 'api@oanda.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='oanda forex wrapper rest api',
    py_modules = [
        'oandapy'
    ],
    install_requires = [
        'requests'
    ],
)