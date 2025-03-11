import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import functools


def get_text():
    """
    Returns the contents of the Tau Manifesto as a string of words, separated by spaces.

    The resultant string contains no numbers, punctuation or LaTeX expressions.
    """

    # Gets HTML source of the website
    page = requests.get("https://tauday.com/tau-manifesto")
    soup = BeautifulSoup(page.text, 'html.parser')

    # Gets the entire manifesto in text form
    body_text = '\n'.join([section.text for section in soup.find_all("div", {"class": "section"})])

    # Removes all LaTeX expressions by searching for \[...\] and \(...\) delimiters
    body_text = re.sub(r"\\\[.+?\\\]", "", body_text, flags=re.DOTALL)
    body_text = re.sub(r"\\\(.+?\\\)", "", body_text, flags=re.DOTALL)

    # Removes all LaTeX equations by searching for equation and align* environments
    body_text = re.sub(r"\\begin\{equation\}.+?\\end\{equation\}", "", body_text, flags=re.DOTALL)
    body_text = re.sub(r"\\begin\{align\*\}.+?\\end\{align\*\}", "", body_text, flags=re.DOTALL)

    # Removes all punctuation, preserving only letters, spacing and hyphens
    body_text = body_text.lower()
    body_text = re.sub(r"[—\-]", " ", body_text)
    body_text = re.sub(r"[^a-z\s]", "", body_text)
    body_text = re.sub(r"\s+", " ", body_text)

    return body_text


def get_counter():
    """
    Returns a collections.Counter object representing the letter frequencies of the Tau Manifesto.
    """
    c = Counter(get_text())
    del c[' ']
    return c


def get_letter_freqs():
    """
    Returns a list of 2-tuples, where each tuple consists of a letter followed by the number of times that letter
    appears in the Tau Manifesto.

    Tuples are arranged in descending order of letter frequency.
    """
    return [count for letter, count in get_counter().most_common()]


@functools.cache
def get_freq_ranking_dict():
    """
    Returns a dictionary of (key, value) pairs where each key is an integer r and the corresponding value refers to the
    number of appearances made by the r-th most common letter in the Tau Manifesto.

    This function is cached because:
    - it is called many times during the pi estimation process
    - it returns the same dictionary every time
    """
    result = dict()
    for i, count in enumerate(get_letter_freqs()):
        result[i+1] = count
    return result


if __name__ == '__main__':
    print(get_counter())
