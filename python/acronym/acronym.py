import re


def abbreviate(words):
    '''creates acronyn from words'''

    reg = r"(\b[a-zA-Z])?((?<=_)[a-zA-Z])?(?<!'[a-z])"
    acr = re.search(reg, words).group()
    print(acr)
    return acr

abbreviate(
    "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me")

