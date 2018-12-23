import unittest

from nose.plugins.attrib import attr
from parameterized import param, parameterized

from server.logic import fizzbuzz


@attr(size='small')
class TestFizzBuzz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(
        [
            param("value_1", input=1, expected="1"),
            param("value_2", input=2, expected="2"),
            param("value_3", input=3, expected="Fizz"),
            param("value_4", input=4, expected="4"),
            param("value_5", input=5, expected="Buzz"),
            param("value_6", input=6, expected="Fizz"),
            param("value_10", input=10, expected="Buzz"),
            param("value_15", input=15, expected="FizzBuzz"),
            param("value_30", input=15, expected="FizzBuzz"),
        ]
    )
    def test_fizzbuzz_normal(self, _, input, expected):
        actual = fizzbuzz.fizzbuzz(input)
        self.assertEqual(actual, expected)
