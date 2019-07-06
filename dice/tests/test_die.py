import unittest
from dice import die


class TestDie(unittest.TestCase):
    def setUp(self):
        self.instance = die.Die()

    def test_throw(self):
        """Make sure side is not zero after throw"""
        self.instance.throw()
        self.assertNotEqual(self.instance.side, 0)

    def test_zero_raises_value_error(self):
        self.assertRaises(ValueError, die.roll, 0)

    def test_get_value(self):
        """Get the value of the side in correct range"""
        val = self.instance.get_value()
        self.assertEqual(val, 0)
        for throw in range(100):
            self.instance.throw()
            val = self.instance.get_value()
            self.assertIn(val, list(range(1, self.instance.num_sides + 1)))

    def test_roll(self):
        """Roll should return a number 1 <= x <= 12"""
        for d in die.roll():
            self.assertIn(d, list(range(1, 13)))

    def test_logging(self):
        """Make sure the logger is properly initialized"""
        self.instance.log.warning("TEST")
