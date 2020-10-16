import unittest
from unittest import TestCase
from main import *

# determine if we are loading the fake data for unit testing
yes_fake_data = 1
no_fake_data = 0
is_data_fake = yes_fake_data

class MainTest(TestCase):

    def test_init(self):
        test_data_universe = DataUniverseConfiguration("", "", "", "", "", "", is_data_fake)
        # check that the variables have been set to empty
        self.assertEqual(test_data_universe.file, "", ".file attribute not assigned properly")

    def test_config_file(self):
        test_data_universe = DataUniverseConfiguration("", "", "", "", "", "", is_data_fake)
        test_data_universe.populate("")
        # check that the variables have been set to empty
        self.assertEqual(test_data_universe.file, "", ".file attribute not assigned properly")

suite = unittest.TestLoader().loadTestsFromTestCase(MainTest)
unittest.TextTestRunner(verbosity=2).run(suite)

