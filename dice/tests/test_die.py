import unittest
from dice import die


class TestDie(unittest.TestCase):

    def setUp(self):
        self.instance = die.Die()

    def test_throw(self):
        """Make sure side is not zero after throw"""
        self.instance.throw()
        self.assertNotEqual(self.instance.side, 0)

    def test_get_value(self):
        """Get the value of the side in correct range"""
        val = self.instance.get_value()
        self.assertEqual(val, 0)
        for throw in range(100):
            self.instance.throw()
            val = self.instance.get_value()
            self.assertIn(val, range(1, self.instance.num_sides + 1))

    def test_ifname_main(self):
        """Try to emulate calling from shell"""
        __name__ == '__main__'

    def test_roll(self):
        """Roll should return a number between 1 and 12 inclusive"""
        for d in die.roll():
            self.assertIn(d, range(1, 13))

    def test_run(self):
        """Test the 'test' action"""
        die.run('test')
