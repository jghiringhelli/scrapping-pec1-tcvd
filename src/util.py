import re


def cleantext(text):
    return re.sub('\s+', '', text)
