#!/usr/bin/python3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import imdb_scrape_country as imdbC
from IPython.display import clear_output


def split_duration(duration, content_type):
    if ((content_type == 'Movie') & (isinstance(duration, str))):
        retval = duration.split(" ")[0]
    else:
        retval = ""
    return retval


def split_seasons(duration, content_type):
    if ((content_type == 'TV Show') & (isinstance(duration, str))):
        retval = duration.split(" ")[0]
    else:
        retval = ""
    return retval


def num_countries(countries):
    if (isinstance(countries, str)):
        num_c = len(countries.split(','))
    else:
        num_c = 0
    return num_c


if __name__ == '__main__':
    netflix = pd.read_csv('data/netflix/netflix_titles.csv')
    prime = pd.read_csv('data/amazonprime/amazon_prime_titles.csv')
    disneyplus = pd.read_csv('data/disneyplus/disney_plus_titles.csv')

    netflix['platform'] = 'Netflix'
    prime['platform'] = 'Prime'
    disneyplus['platform'] = 'Disney+'

    ott = netflix.append(prime).append(disneyplus)

    vec_split_duration = np.vectorize(split_duration)
    vec_split_seasons = np.vectorize(split_seasons)
    vec_num_countries = np.vectorize(num_countries)

    ott['duration_min'] = vec_split_duration(ott.duration, ott.type)
    ott['num_seasons'] = vec_split_seasons(ott.duration, ott.type)
    ott['num_countries'] = vec_num_countries(ott.country)

    ott.to_csv('data/ott.csv')
