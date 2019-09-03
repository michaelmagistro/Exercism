import re


def abbreviate(words):
    '''creates acronyn from words'''

    reg = r"^[A-Z]?|(?<=[ _\n\-])[a-zA-Z]"
    acr = re.findall(reg, words)
    acr = ''.join(acr).upper()
    print(acr)
    return acr

abbreviate(
    "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me")
