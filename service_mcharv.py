# A BeautifulSoup scraping library designed to extract user reviews and their dates and scores from
# Metacritic. It is designed to work within the Metacritic DOM as long as it is given a base URL
# The Metacritic DOM, however, may well have changed. If this is the case, the script may need
# substantial modification, or may not function at all with the non-JavaScript based BeautifulSoup
# framework.

# includes
# ConfigParser is included to get confidential information from a cloud store;
# any version of this script which is distributed will not function until this is updated to 
# a cloud store with a legitimate configuration file for the data schema, OR until such data
# is hardcoded by the script's posessor.
from configparser import ConfigParser
# import scraping libraries
# requests may be able to be removed later, depending on the efficiency of the software
import requests
from bs4 import BeautifulSoup
# also may be able to exclude lxml, but it has improved parsing results in the past
# I advise including it, as a "good luck charm"
import lxml
# import client-side data handling
import pandas as pd

def user_input_base_url():
    print('Service Script for Entertainment Marketing Data Analysis')
    print('target site and purpose: Metacritic video game user reviews')
    print('author: Ellie Lockhart, Ph.D.')
    print('updated: 28 October 2020\n\n')
    print('It is the user\'s responsiblity to make sure they are following all network rules and regulations related to automated data extraction on the platform on which they run the software. By entering a URL to scan, you understand that a large amount of data may be retrieved from a third party\'s server, and you warrant that you have permission from both the targeted server\'s operator and the operator of any server or other device from which you may be operating this script that this use case is acceptable.\n\n')
    print('In order to extract the data from reviews, this service script requires a MetaCritic base game URL.')
    print('These URLs consist of both a game\'s platform, and a web-friendly version of its title.')
    print('An example of such a URL is: https://www.metacritic.com/game/xbox-360/tomb-raider')
    print('Keep in mind that this will NOT extract any reviews for the PC, PlayStation 3, or PlayStation 4 versions of this title. Furthermore, the pandas dataframe and database integrations will store these reviews separately. If needed, you may adjust the database interface as appropriate if you wish to combine reviews of games across multiple platforms.\n\n')
    print('OK! Let\'s get to work: please copy and paste a relevant Metacritic base URL, assuming you agree to the consent affirmation above as well as the license terms under which this script is distributed.\n')
    input_url = input('Base URL (Metacritic only):')
    # pass the URL out of the function so it can be used elsewhere
    return input_url



