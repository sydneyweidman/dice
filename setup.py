from setuptools import setup

execfile('dice/version.py')

setup(
    name="dice",
<<<<<<< Updated upstream
    version="0.1.1",
    packages=["dice"],
    test_suite='dice.tests',
    entry_points={
        'console_scripts': [
            'roll=dice.command:main'
        ]
    }
)
=======
    version=__version__,
    packages=["dice"],
    data_files=[('appconfig', ['resources/reader.ini']),
                ('logconfig', ['resources/log.ini'])],
    test_suite='dice.tests', )
>>>>>>> Stashed changes
