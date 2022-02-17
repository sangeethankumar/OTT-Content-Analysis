#!/usr/bin/python3

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import imdb_scrape_country as imdbC
from IPython.display import clear_output


def split_duration(duration, content_type):
    """
    convert duration to minutes for movies

    _extended_summary_

    Parameters
    ----------
    duration : _type_
        _description_
    content_type : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if ((content_type == 'Movie') & (isinstance(duration, str))):
        retval = duration.split(" ")[0]
    else:
        retval = ""
    return retval


def split_seasons(duration, content_type):
    """
    convert duration to number of seasons for TV shows

    _extended_summary_

    Parameters
    ----------
    duration : _type_
        _description_
    content_type : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if ((content_type == 'TV Show') & (isinstance(duration, str))):
        retval = duration.split(" ")[0]
    else:
        retval = ""
    return retval


def num_vals(vals):
    """
    Number of countries listed in country of origin

    _extended_summary_

    Parameters
    ----------
    countries : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if (isinstance(vals, str)):
        num_c = len(vals.split(','))
    else:
        num_c = 0
    return num_c


def convert_rating(given_rating):
    """
    convert rating to amazon prime maturity rating format

    _extended_summary_

    Parameters
    ----------
    given_rating : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    rating_key = ['TV-MA', 'TV-14', '13+', 'R', '16+', 'TV-PG', 'ALL', '18+', 'PG-13', 'PG', 'TV-G', 'TV-Y7', 'TV-Y', 'G', '7+', 'NA', 'NR',
                  'TV-NR', 'UNRATED', 'TV-Y7-FV', 'NC-17', 'UR', 'AGES_18_', 'NOT_RATE', 'AGES_16_', '66 min', '84 min', '74 min', '16', 'ALL_AGES']
    rating_val = ['Adults', 'Young Adults', 'Teens', 'Adults', 'Young Adults', 'Older Kids', 'General', 'Adults', 'Teens', 'Older Kids', 'General', 'Older Kids', 'General', 'General',
                  'Older Kids', 'Unrated', 'Unrated', 'Unrated', 'Unrated', 'Older Kids', 'Adults', 'Unrated', 'Adults', 'Unrated', 'Young Adults', 'Unrated', 'Unrated', 'Unrated', 'Young Adults', 'General']
    if given_rating in rating_key:
        ind = rating_key.index(given_rating)
        return rating_val[ind]
    else:
        return 'Unrated'


def str2list(str_vals):
    """
    Convert a string with multiple values into list

    _extended_summary_

    Parameters
    ----------
    str_vals : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    list_val = [x.lstrip() for x in str_vals.split(',')]
    return list_val


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
    vec_num_valses = np.vectorize(num_vals)

    ott['duration_min'] = vec_split_duration(ott.duration, ott.type)
    ott['num_seasons'] = vec_split_seasons(ott.duration, ott.type)
    ott['num_countries'] = vec_num_vals(ott.country)

    ott['New Rating'] = np.vectorize(convert_rating)(ott.rating)

    ott['countries_list'] = ott['country'].apply(str2list)
    ott['genres'] = ott['listed_in'].apply(str2list)

    ott.to_csv('data/ott.csv')
