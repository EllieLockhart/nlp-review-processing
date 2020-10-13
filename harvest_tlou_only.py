# harvest & insert Polygon user reviews into a PostgreSQL database
# (running locally in this script, could be adapted for remote/cloud
# use) along with as much metadata as Rotten Tomatoes will allow to be
# scraped.

# implemented with BeautifulSoup based processing

# import necessary libraries
# DONE: import system and networking libraries
import os
import sys
from configparser import ConfigParser
# import the PostgreSQL interface library
import psycopg2
# DONE: import scraping libraries
import requests
from bs4 import BeautifulSoup
import lxml

# connect to a local PostgreSQL server that will function as a repository for the media data
# in this case the authentication details are simply examples; you should adjust them for your own
# database
# the script is written with the assumption that an SSL link is *not* required
# TODO: connect to Postgre server & database
def config(filename='database.ini', section='postgresql'):
    # create a configuration file parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get Postgresql section contents
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def connect_postgre():
    db_conn = None
    try:
        params = config()

        print('Connecting to PostgreSQL database...')
        db_conn = psycopg2.connect(**params)

        db_cur = db_conn.cursor()

        print('PostgreSQL db version')
        db_cur.execute('SELECT version()')
        db_version = db_cur.fetchone()
        print(db_version)

        print('Login successful to media-viewpoints database.')
        print('This script is configured to scrape specific Metacritic for user reviews of The Last of Us Part II.')


        # TODO: implement a decrement or set-based system for determining the number of reviews to fetch

        # begin the main data harvesting and database upload loop
        rvwn = 1  # review counter for file names
        for rNumber in range(1, 741):
            # set the Metacritic base URL to be extracted for this script
            url = 'https://www.metacritic.com/game/playstation-4/the-last-of-us-part-ii/user-reviews?page={}'.format(
                rNumber)

            # identify self as a standard browser
            user_agent = {'User-agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=user_agent)  # get the page into memory

            soup = BeautifulSoup(response.text, 'lxml')  # standard Soup parsing

            # look for blurb blurb_expanded tags since every user review has this tag
            reviews = soup.find_all('span', attrs={'class': 'blurb blurb_expanded'})

            for rvw in reviews:
                numberSuffix = str(rvwn)
                db_insert_query = """ INSERT INTO tlou2_metacritic_10_13 (review_number, review_text) VALUES (%s,%s)"""
                db_review_selection = (rvwn, rvw.text)
                db_cur.execute(db_insert_query, db_review_selection)
                db_conn.commit()
                count = db_cur.rowcount
                print (count, "Review archived in database.")
                print(rvw.text)
                rvwn += 1
                # review_dict['review'].append(review.find('span', class_='blurb blurb_expanded').text)

        # close network connections
        # TODO: close network connections
        db_cur.close()
    except (Exception, psycopg2.DatabaseError) as db_error:
        print(db_error)
    finally:
        # close database connections
        if db_conn != None:
            db_conn.close()
            print('PostgreSQL connection termination.')

if __name__ == '__main__':
    connect_postgre()




# DONE: close database connections
# TODO: implement a configuration file that says which game to scrape
# TODO: implement a method to determine how many pages of reviews there are for a game, instead of hard coding
# TODO: support critic reviews as well