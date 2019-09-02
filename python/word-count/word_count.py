import re
from collections import Counter

def count_words(sentence):
    reg = r"'(?=[\s])|(?<=[\s])'|[^a-z0-9']+"
    sentence = sentence.lower()
    sentence = re.sub(reg, ' ', sentence)
    result = sentence.split()
    result = [ x.strip("'") for x in result ]
    counter = dict(Counter(result))
    return counter
