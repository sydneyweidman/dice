import random


class Die(object):
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
        self.side = 0
        self.num_sides = num_sides

    def throw(self):
        """Simulate throwing a die"""
        self.side = random.randint(1, self.num_sides)

    def get_value(self):
        return self.side


def test(name):
    import doctest
    doctest.testmod(name)

if __name__ == '__main__':
    test('die')
