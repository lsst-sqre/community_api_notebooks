from setuptools import setup, find_packages
import os
from io import open


packagename = 'community'
description = 'community.lsst.org api automations'
author = 'Jonathan Sick'
author_email = 'jsick@lsst.org'
license = 'MIT'
url = 'https://github.com/lsst-sqre/community_api'
version = '0.1.0'


def read(filename):
    full_filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename)
    return open(full_filename, mode='r', encoding='utf-8').read()

long_description = read('README.md')


setup(
    name=packagename,
    version=version,
    description=description,
    long_description=long_description,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='lsst',
    packages=find_packages(exclude=['docs', 'tests*', 'notebooks']),
    install_requires=['requests'],
    # package_data={},
    # entry_points={},
)
