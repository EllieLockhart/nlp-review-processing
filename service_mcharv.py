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
