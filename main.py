# Natural Language Processing of Mass Media reviews
# By Ellie Lockhart, October 2020

# import dependencies
from textblob import TextBlob


# function to load the configuration file
class DataUniverseConfiguration(object):

    def __init__(self, file, address, database, user, password, table):
        self.file = file
        self.address = address
        self.database = database
        self.user = user
        self.password = password
        self.table = table

    #def blob_make(self, table):
