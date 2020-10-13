# Natural Language Processing of Mass Media reviews
# By Ellie Lockhart, October 2020

# import dependencies
from textblob import TextBlob
from tomlkit import parse
import psycopg2 # Psy Cop G2, the scariest of Psy Cops

# short term solution to refactor later: global configuration vars for database
pcd_address = ""
pcd_database_specific = ""
pcd_database_user = ""
pcd_database_password = ""
pcd_database_table = ""

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
        pcd_address = self.address
        pcd_database_user = self.user
        pcd_database_specific = self.database
        pcd_database_password = self.password

    def login(self):
        print(f"Initiating login to the {self.database} database on server {self.address} to access {self.table}...")
        conn = None
        try:
            print(f"Establishing connection with {self.address}...")
            conn = psycopg2.connect(host=self.address, database=self.database, user=self.user, password=self.password)
            print("Establishing an SQL input cursor...")
            cur = conn.cursor()
            # get the server version to verify it is working properly
            cur.execute('SELECT version()')
            server_psql_version = cur.fetchone()
            print(f"Postgres version on {self.address} is {server_psql_version}")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error returned: /n {error}")
            print("Program failed.")
        finally:
            print("Server login test complete, logging out.")
            conn.close

class ResearchObject(object):

    def __init__(self, ngram_depth, correct_spelling, word_freq_1, word_freq_2, word_freq_3, word_freq_4, word_freq_5, word_freq_6, word_freq_7, word_freq_8, word_freq_9, word_freq_10, word_freq_11, word_freq_12, word_freq_13, word_freq_14, word_freq_15, word_freq_16, word_freq_17, word_freq_18):
        self.ngram_depth = ngram_depth
        self.correct_spelling = correct_spelling
        self.word_freq_1 = ""
        self.word_freq_2 = ""
        self.word_freq_3 = ""
        self.word_freq_4 = ""
        self.word_freq_5 = ""
        self.word_freq_6 = ""
        self.word_freq_7 = ""
        self.word_freq_8 = ""
        self.word_freq_9 = ""
        self.word_freq_10 = ""
        self.word_freq_11 = ""
        self.word_freq_12 = ""
        self.word_freq_13 = ""
        self.word_freq_14 = ""
        self.word_freq_15 = ""
        self.word_freq_16 = ""
        self.word_freq_17 = ""
        self.word_freq_18 = ""

    # never call this function without an open database connection!
    def populate(self):
        conn = None
        try:
            pcd_database_specific = "media-viewpoints"
            print(f"Establishing connection...")
            conn = psycopg2.connect(host=pcd_address, database=pcd_database_specific, user=pcd_database_user, password=pcd_database_password)
            print("Establishing an SQL input cursor...")
            cur = conn.cursor()
            print(f"Finding language corpus entries in {pcd_database_table}...")
            selection_query = f"SELECT * FROM reviews_tlou2_no_username_raw"
            cur.execute(selection_query)
            print(F"Reading all selected text from {pcd_database_table} into memory. This may take some time.")
            selection_records = cur.fetchall()
            raw_blob = ""
            for row in selection_records:
                raw_blob += row[1]
                raw_blob += "\n"

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error returned: /n {error}")
            print("Program failed.")
        finally:
            print("Server login test complete, logging out.")
            print(raw_blob)
            conn.close

        # print("Preprocessing blob: spell check")
        # prepro_blob = TextBlob(raw_blob)
        # prepro_blob1 = prepro_blob.correct()
        # print("Spell check complete.")

        main_blob = TextBlob(raw_blob)
        print(main_blob.ngrams(n=3))





def main():
    this_research = ResearchObject(0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    this_universe = DataUniverseConfiguration("","","","","","",0)
    this_universe.populate()
    this_universe.login()
    this_research.populate()

if __name__ == "__main__":
    main()









