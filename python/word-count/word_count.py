import re
from collections import Counter

def count_words(sentence):
    reg_all_single_quotes = r"'(?=[^\w])|(?<=[^\w])'|'$"
    reg_all_special_limited = r"[^\w\s\']"
    reg_double_spaces = r"\s\s+"
    reg_start_space = r"^ "
    sentence = sentence.replace('\n', ' ')
    sentence = sentence.replace('\t', ' ')
    sentence = sentence.replace('\r', ' ')
    sentence = sentence.replace(',', ' ')
    sentence = sentence.replace('_', ' ')
    sentence = re.sub(reg_all_single_quotes, "", sentence)
    sentence = re.sub(reg_all_special_limited, "", sentence)
    sentence = sentence.lower()
    sentence = re.sub(reg_double_spaces, " ", sentence)
    sentence = re.sub(reg_start_space, "", sentence)
    sentence = re.split(r"\s", sentence)
    distinct = []
    for x in sentence:
        if distinct.count(x) == 0:
            distinct.append(x)
    result = {}
    for word in distinct:
        occurences = sentence.count(word)
        result.update({word : occurences})
    return result


