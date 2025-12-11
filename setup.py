from setuptools import find_packages, setup

NAME = 'geonode-dynamic-rest'
DESCRIPTION = 'Dynamic API support to Django REST Framework.'
URL = 'https://github.com/GeoNode/dynamic-rest'
VERSION = '2.3.0.1'
SCRIPTS = ['manage.py']

setup(
    description=DESCRIPTION,
    include_package_data=True,
    install_requires=open('install_requires.txt').readlines(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    name=NAME,
    packages=find_packages(),
    scripts=SCRIPTS,
    url=URL,
    version=VERSION,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
