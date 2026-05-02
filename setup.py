from setuptools import setup

setup(
    name='rich-argparse',
    version='1.8.0',
    description='Rich help formatters for argparse and optparse',
    author_email='Ali Hamdan <ali.hamdan.dev@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Software Development :: User Interfaces',
    ],
    install_requires=[
        'rich>=11.0.0',
    ],
    packages=[
        'rich_argparse',
    ],
)
