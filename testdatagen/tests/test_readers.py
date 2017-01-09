from datagen import datareader
import unittest


class TestReaders(unittest.TestCase):
    def test_can_read_etternavn(self):
        etternavn = datareader.read_etternavn()
        self.assertEqual(3467, len(etternavn))
        self.assertEqual("Hansen", etternavn[0])
        self.assertEqual("Jørgensen", etternavn[20])
        self.assertEqual("Abdulla", etternavn[-1])

    def test_can_read_guttenavn(self):
        guttenavn = datareader.read_guttenavn()
        self.assertEqual(576, len(guttenavn))
        self.assertEqual("Aaron", guttenavn[0])
        self.assertEqual("Zander", guttenavn[-1])

    def test_can_read_jentenavn(self):
        jentenavn = datareader.read_jentenavn()
        self.assertEqual(630, len(jentenavn))
        self.assertEqual("Abigail", jentenavn[0])
        self.assertEqual("Zuzanna", jentenavn[-1])