"""
Setup file for race-tracker.
"""
from setuptools import setup


setup(
    name='race-tracker',
    version='0.0.1',
    author='Damien Plenard',
    author_email='damien@plenard.me',
    license="MIT",
    packages=['settings', 'bot', 'api'],
    test_suite="tests",
    description=(
        "A service to be notified of the start of a race on SpeedRunsLive."
    ),
    entry_points={
        'console_scripts': [
            'srlbot = bot:main',
        ]
    }
)
