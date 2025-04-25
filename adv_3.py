"""
concurrent.futures:
https://docs.python.org/3/library/concurrent.futures.html
newspaper:
https://newspaper.readthedocs.io/en/latest/
"""

import newspaper
from newspaper import Article
import concurrent.futures


def load_headlines(url):
    """
    Loads headline data, appends to a list of headlines, and returns the list.
    Builds a Source object containing the article headlines, specifying memoize_articles as false so we can crawl
    over headlines multiple times.
    Downloads the article, parses it, and adds the article's title to the headline list. Returns the headline list.
    """
    result = newspaper.build(url, memoize_articles=False)
    headline_list = []
    for i in range(1, 6):
        art = result.articles[i]
        art.download()
        art.parse()
        headline_list.append(art.title)
    return headline_list


def get_headlines():
    """
    Fetches and prints the headlines using 5 workers. Creates 5 workers and passes a url with each worker to load_headlines().
    Prints the website and fetched headline.
    """
    URLs = ['https://theguardian.com',
            'http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/', ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_headlines, url): url for url in URLs}
        # future_to_url = {executor.map(load_headlines, url): url for url in URLs}
        for future in concurrent.futures.as_completed(future_to_url):
            print(future_to_url[future])
            art = future.result()
            for i in art:
                print(i)


def sequential():
    """
    Downloads and builds the headlines found in the urls sequentially, without using workers.
    Builds a Source object containing the article headlines, specifying memoize_articles as false so we can crawl
    over headlines multiple times.
    Downloads the article, parses it, and prints the article's title.
    """
    URLs = ['https://theguardian.com',
            'http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/', ]
    for url in URLs:
        result = newspaper.build(url, memoize_articles=False)
        print('\n''The headlines from %s are' % url, '\n')
        for i in range(1, 6):
            art = result.articles[i]
            art.download()
            art.parse()
            print(art.title)


if __name__ == '__main__':
    import timeit

    elapsed_time1 = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=1) / 1
    print(elapsed_time1)
    elapsed_time2 = timeit.timeit("sequential()", setup="from __main__ import sequential", number=1) / 1
    print(elapsed_time2)