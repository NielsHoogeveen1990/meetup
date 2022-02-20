from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='meetup',
    keywords='',
    version='1.0',
    author='Niels Hoogeveen',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    description='.',
    entry_points={'console_scripts': ['hello-meetup = meetup:hello']},
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)
