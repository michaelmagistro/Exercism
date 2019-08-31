def convert(number):
    pling = 3
    plang = 5
    plong = 7
    profile = ""
    if number % pling == 0:
        profile = profile + 'Pling'
    if number % plang == 0:
        profile = profile + 'Plang'
    if number % plong == 0:
        profile = profile + 'Plong'
    if profile != "":
        return profile
    else:
        return str(number)
