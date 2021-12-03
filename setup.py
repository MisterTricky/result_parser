from setuptools import setup

setup(
    name='results_reader',
    version="0.0.2",
    packages=['result_parser'],
    entrypoints={
        'console_scripts': [
            'cli = result_parser:main'
        ]
    }
)
