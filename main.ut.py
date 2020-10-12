import unittest
from unittest import TestCase
from main import *


class MainTest(TestCase):

    def test_init(self):
        test_data_universe = DataUniverseConfiguration("", "", "", "", "", "")
        # check that the variables have been set to empty
        self.assertEqual(test_data_universe.file, "", ".file attribute not assigned properly")

suite = unittest.TestLoader().loadTestsFromTestCase(MainTest)
unittest.TextTestRunner(verbosity=2).run(suite)

