# Natural Language Processing of Mass Media reviews
# By Ellie Lockhart, October 2020

# import dependencies
from textblob import TextBlob
from tomlkit import parse
import psycopg2 # Psy Cop G2, the scariest of Psy Cops

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


    def populate(self):
        # temporary test to ensure the library has been properly imported
        if self.global_test == 1:
            self.file = "default.toml"
        else:
            self.file = "config.toml"


        config_file = open(self.file, 'r')

        every_last_var_of_them = config_file.read()

        config_file.close()

        parsed_config = parse(every_last_var_of_them)

        self.address = parsed_config["database"]["database_server_address"]
        self.database = parsed_config["database"]["database_specific_database"]
        self.user = parsed_config["database"]["database_login"]
        self.password = parsed_config["database"]["database_password"]
        self.table = parsed_config["job"]["table_to_process"]

    def login(self):
        conn = psycopg2.connect(host=self.address, database=self.database, user=self.user, password=self.password)

def main():
    this_universe = DataUniverseConfiguration("","","","","","",0)

if __name__ == "__main__":
    main()









