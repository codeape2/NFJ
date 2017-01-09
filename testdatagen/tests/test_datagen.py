import unittest
from datagen.datagen import generate_persons
import itertools


class TestDataGen(unittest.TestCase):
    def test_can_generate(self):
        hundred_persons = list(itertools.islice(generate_persons(), 0, 100))
        self.assertEqual(100, len(hundred_persons))

        p0 = hundred_persons[0]
        p1 = hundred_persons[1]
        self.assertEqual("Aaron Hansen", p0.name)
        self.assertEqual("M", p0.sex)
        self.assertEqual("Abigail Hansen", p1.name)
        self.assertEqual("F", p1.sex)

        p99 = hundred_persons[99]
        self.assertEqual("Ana Fredriksen", p99.name)