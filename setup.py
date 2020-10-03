#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'opencv-python>=4.4.0.44',
    'numpy>=1.19.2',
    'pathlib>=1.0.1',
    'click>=7.1.2'
]

test_requirements = [
    'tox>=3.20.0',
    'flake8>=3.8.4'
]

setup(
    name='matrix_rotation',
    version='0.2',
    description="Rotate any square matrix clockwise and anticlockwise in any degree.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Vaibhav Hiwase",
    author_email='hiwase.vaibhav@gmail.com',
    url='https://github.com/vhiwase/matrix-rotation',
    packages=[
        'matrix_rotation',
    ],
    package_dir={'matrix_rotation': 'matrix_rotation'},

    entry_points={
        'console_scripts': [
            'matrix_rotation=matrix_rotation.matrix_rotation_cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='matrix_rotation',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.5',
    test_suite='tests',
    tests_require=test_requirements
)
