#! /usr/bin/python3
from distutils.core import setup

setup(
    name='weatherFetcher',
    version='0.1dev',
    author='Tony Clemons',
    author_email='clemons745@gmail.com',
    description='A weather information fetcher program',
    packages=['weatherFetcher'],
    license='GNU General Public License v3 (GPLv3)',
    long_description=open('readme.txt').read(),
    keywords='weather fetch fetcher openweathermap.org openweathermap cron crontab',
    url="https://github.com/clemons745/weatherFetcher",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Environment :: Console',
        'Programming Language :: Python :: 3'
    ],
)
