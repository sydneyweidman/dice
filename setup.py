from setuptools import setup

execfile('dice/version.py')

setup(
    name="dice",
    version="0.1.1",
    packages=["dice"],
    test_suite='dice.tests',
    entry_points={'console_scripts': ['roll=dice.command:main']})
