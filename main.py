# Natural Language Processing of Mass Media reviews
# By Ellie Lockhart, October 2020

# import dependencies
from textblob import TextBlob
import toml

# function to load the configuration file
class DataUniverseConfiguration(object):

    def __init__(self, file, address, database, user, password, table, global_test):
        self.file = file
        self.address = address
        self.database = database
        self.user = user
        self.password = password
        self.table = table
        # check if this is a test of data import
        self.global_test = global_test


    def populate(self, file):
        # temporary test to ensure the library has been properly imported
        if self.global_test == 1:
            self.file = "default.toml"
        else:
            self.file = "config.toml"


        local_config = toml.loads("default.toml")

        # read the values into the program's memory
        local_config['database']
        local_config.get('database')







