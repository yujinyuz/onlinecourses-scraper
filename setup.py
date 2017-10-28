#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(yujinyuz): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='onlinecourses_ooo',
    version='0.1.0b1',
    description="My personal scraper for https://onlinecourses.ooo",
    long_description=readme + '\n\n' + history,
    author="Eugene Essun Oliveros",
    author_email='jinyuzprodigy@gmail.com',
    url='https://github.com/yujinyuz/onlinecourses-ooo',
    packages=find_packages(include=['onlinecourses_ooo']),
    entry_points={
        'console_scripts': ['onlinecourses=onlinecourses_ooo:main'],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='onlinecourses_ooo',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
