from setuptools import setup, find_packages

setup(
    name='pymongodump',
    version='0.1',
    description='utility to dump and restore mongodb databases from python (with pymongo)',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Database",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    author='Daniel Crosta',
    author_email='dcrosta@late.am',
    url='',
    keywords='mongodb dump restore pymongo',
    py_modules=['pymongodump'],
)

