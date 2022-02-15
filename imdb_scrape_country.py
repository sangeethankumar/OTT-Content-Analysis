#!/usr/bin/python3
"""
scraping imdb for country of origin of a title

given the title of the movie, returns the country of origin

Returns
-------
_type_
    _description_
"""

from bs4 import BeautifulSoup
import imdb
import requests
import re


def get_url_from_title(title: 'str'):
    """
    the imdb url of the title

    uses imdb package to search and return the url to imdb page of the title

    Parameters
    ----------
    title : str
        title of the movie/TV-show

    Returns
    -------
    str
        url to the title
    """
    imdb_cls = imdb.IMDb()
    all_search_res = imdb_cls.search_movie(title)
    first_title = all_search_res[0]
    url = imdb_cls.get_imdbURL(first_title)
    return url


def get_country(title: 'str'):
    """
    country of origin of the title

    returns all the countries of origin from the imdb page of the title

    Parameters
    ----------
    title : str
        title of the movie/TV show

    Returns
    -------
    _type_
        countries of origin
    """
    x = ""
    url = get_url_from_title(title)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    divcontainer = soup.find_all('a',
                                 class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    hls = [divcontainer][0]
    country = [str(hl).split('>')[-2].split('<')[0]
               for hl in hls if str(hl).find('country_of_origin') != -1]
    countries = ",".join(country)
    return countries


if __name__ == '__main__':
    title = 'My Little Pony: A New Generation'
    print(get_country(title))
