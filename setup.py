#coding: utf-8

from setuptools import setup, find_packages

import admin_thumbnail

setup(
    name='django_admin_thumbnail',
    version=admin_thumbnail.__VERSION__,
    author='Flávio Caetano',
    author_email='flavio@vieiracaetano.com',
    packages=find_packages(),
    url='https://github.com/fjcaetano/django_admin_thumbnail',
    license='MIT - see LICENSE.txt',
    description='Thumbnails for ImageFields in django admin.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.4",
        "sorl-thumbnail >= 11.12",
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Portuguese (Brazilian)',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    platforms='any',
    zip_safe=False,
)