
"""
This code will use bs4 & requests libraries to 
extract table from wikipedia pages
and create a data frame from the wikipedia table

Author: Lauren Wilson
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_wiki(url):
    
    # send a GET request to the wikipedia url and be sure response says 200 for legality
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(url)
    print(response.status_code)
    
    if response.status_code == 200:

        # parsing HTML data
        soup = BeautifulSoup(response.text, 'html.parser') # making soup
        wiki_table = soup.find('table', {'class':'wikitable'}) # finding table

        # convert wikipedia table into a Python dataframe
        df = pd.read_html(str(wiki_table))# read the html into a dataframe object with pandas

        # convert list to dataframe
        df = pd.DataFrame(df[0])

        return df

