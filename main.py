import os
from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
from collections import Counter
import logging

MAX_URL_DEPTH = 4
visited_links = {}      # Maintains the array of all the visited links for avoiding duplicacy
domain = urlparse(os.getenv('url')).netloc

logging.basicConfig(filename="main.log",
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def filter_link(link):
    """

    :param link: URL which has to be validated
    :return: True for the URL which is of same domain and also it is not visited before
    """
    return urlparse(link).netloc == domain and link.strip('/') not in visited_links


def process_url(url, level):
    """

    :param url: The URL to be processed ex: https://www.314e.com/
    :param level: The current depth level. Ex: URL extracted by parsing one URL makes level = 1
    :return:    Tuple with the data of word and word pair frequencies
    """
    words = {}
    word_pairs = {}
    try:
        html = urlopen(url).read()
        logger.info("URL read sucessfully: {}".format(url))
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text from the fetched HTML
        text = soup.get_text()
        logger.info("Text extracted successfully. URL: {} ".format(url))
    except Exception as e:
        logger.exception("Not able to parse the HTML file of the given URL")
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    for line in lines:
        prev_word = None
        for word in line.split(' '):
            if word == '' or word == ' ':
                continue
            words[word] = words.get(word, 0) + 1
            if prev_word:
                pair = "{} {}".format(prev_word, word)
                word_pairs[pair] = word_pairs.get(pair, 0) + 1
            prev_word = word
    print(lines)

    visited_links[url] = None
    if level < MAX_URL_DEPTH:
        links = [link.get('href') for link in soup.findAll('a')]
        links = list(filter(filter_link, links))
        visited_links.update({l: None for l in links})
        print(links)
        print(" LEVEL = {}".format(level))
        for link in links:
            logger.info("Processing started for level: {}, for URL: {}".format(level, link))
            counters = process_url(link, level+1)
            return((counters[0] + Counter(words), counters[1] + Counter(word_pairs)))

    return((Counter(words), Counter(word_pairs)))


if __name__ == '__main__':
    logger.info("Process started with root URL as: {}".format(os.getenv('url')))
    words_count, word_pair_count = process_url(os.getenv('url').strip('/'), 0)
    sorted_words = sorted(words_count.items(), key=lambda kv: kv[1], reverse=True)
    sorted_word_pairs = sorted(word_pair_count.items(), key=lambda kv: kv[1], reverse=True)
    logger.info("Top ten words pairs with there frequencies are: ".format(sorted_word_pairs[:9]))
    logger.info("\r\n")
    logger.info("Top ten individual words with there frequencies are: ".format(sorted_words[:9]))
