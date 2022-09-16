from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'gstreamer',
    version          = '0.1',
    description      = 'Play video files',
    long_description = readme,
    author           = 'mbenitez1607',
    author_email     = 'mbenitez@redhat.com',
    url              = 'http://wiki',
    packages         = ['gstreamer'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'gstreamer = gstreamer.__main__:main'
            ]
        }
)
