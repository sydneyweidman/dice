import sys
import random
import logging
import logging.config
from pkg_resources import resource_filename


LOGFILE = resource_filename("dice.resources", 'log.ini')


class LoggedComponent(object):
    def __init__(self, configfile=LOGFILE, logger_name=__name__):
        self.configfile = configfile
        logging.config.fileConfig(self.configfile)
        logging.info("Loaded logging config file %s", self.configfile)
        self.logger_name = logger_name
        self.log = logging.getLogger(self.logger_name)


class Die(LoggedComponent):
    """A class to model a die in a board game

    >>> from dice import die
    >>> d = die.Die()
    >>> d.num_sides == 6
    True
    >>> d.throw()
    >>> val = d.get_value()
    >>> val in range(1,7)
    True
    >>>
    """

    def __init__(self, num_sides=6):
        """Initialize the class"""
        super(Die, self).__init__()
        random.seed()
        self.side = 0
        self.num_sides = num_sides
        self.log.info('Initialized Die object...')
        self.log.info('with values: %s', locals())

    def throw(self):
        """Simulate throwing a die"""
        self.side = random.randint(1, self.num_sides)

    def get_value(self):
        return self.side


def roll(count=2):
    """Roll count number of 6-sided dice and return a tuple of the value
    rolled for each die"""
    # Generate a list of dice
    try:
        count = int(count)
    except ValueError:
        print("%s is not an integer" % count)
        return -1
    if count < 1:
        raise ValueError("You must have at least one die")
    print("Rolling {0} dice".format(count))
    dice = [Die() for i in range(count)]
    total = 0
    idx = 0
    for d in dice:
        d.throw()
        idx += 1
        d.log.info("Die {} was {}".format(idx, d.get_value()))
        total += d.get_value()
    if count == 2 and dice[0].get_value() == dice[1].get_value():
        print("Doubles!!")
    print("Total number rolled is {}".format(total))
    return tuple([d.get_value() for d in dice])


def main(count):
    random.seed()
    return roll(count)


def test(module):
    import doctest
    doctest.testmod(module, verbose=True)


if __name__ == '__main__':
    USAGE = "die.py INT"
    try:
        dice = sys.argv[1]
    except IndexError:
        print(USAGE)
    print(main(sys.argv[1]))
