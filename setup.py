from distutils.core import setup
setup(
    name='compropago',
    packages=[
        'compropago',
        'compropago/factory',
        'compropago/factory/models',
        'compropago/tools'
    ],
    version='2.0.0.0',
    description='SDK python para ComproPago',
    author='Eduardo Aguilar',
    author_email='eduardo.aguilar@compropago.com',
    url='https://github.com/compropago/sdk-python',
    download_url='https://github.com/compropago/sdk-python/tarball/2.0.0.0',
    keywords=['payments', 'sdk', 'gateway', 'compropago', 'cash'],
)