from setuptools import setup

exec(compile(open('dice/version.py').read(), 'dice/version.py', 'exec'))

setup(
    name="dice",
    version=__version__,
    packages=["dice"],
    test_suite='dice.tests',
    entry_points={'console_scripts': ['roll=dice.command:main']})
