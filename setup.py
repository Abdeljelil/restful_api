#!/usr/bin/env python

from setuptools import setup, find_packages

module_name = "backend"

setup(
    name=module_name,
    version="0.0.1",
    description='',
    long_description='''
''',
    keywords='python backend API RESTFUL mongodb asyncio',
    author='Mohamed abdeljelil',
    url='',
    license='',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    # install_requires=[
    #     "tornado"
    # ],
    # dependency_links=[
    #     "https://github.com/ilex/aiomotorengine/archive/master.zip"
    # ],
    use_2to3=True,
    extras_require={
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
