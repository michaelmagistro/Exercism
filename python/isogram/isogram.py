def is_isogram(string):
    count = 0
    string2 = string[:]
    length = len(string)
    for a in range(length):
        if string2[a] not in " -":
            for b in range(length):
                if string2[a] == string[b]:
                    count += 1
        else:
            pass
    if count == 1:
        return True
    else:
        return False
