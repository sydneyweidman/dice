from setuptools import setup

execfile('dice/version.py')

setup(
    name="dice",
    version=__version__,
    packages=["dice"],
    test_suite='dice.tests',
    entry_points={'console_scripts': ['roll=dice.command:main']})
