from setuptools import setup

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies = [
    'requests',
    'httpretty'
]

version = '0.2.7'

setup(name='bitfinex',
    version=version,
    description = 'Python client for the Bitfinex API',
    author = 'Scott Barr',
    author_email = 'scottjbarr@gmail.com',
    url = 'https://github.com/philsong/bitfinex',
    license = 'MIT',
    packages=['bitfinex'],
    scripts = ['scripts/bitfinex-poll-orderbook'],
    install_requires = dependencies,
    download_url = 'https://github.com/philsong/bitfinex/tarball/%s' % version,
    keywords = ['bitcoin', 'btc'],
    classifiers = [],
    zip_safe=True)
