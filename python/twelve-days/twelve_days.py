def recite(start_verse, end_verse):
    s = start_verse
    e = end_verse
    prettydays = [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth' ]
    gifts = [ '', 'two Turtle Doves, ', 'three French Hens, ', 'four Calling Birds, ', 'five Gold Rings, ', 'six Geese-a-Laying, ', 'seven Swans-a-Swimming, ', 'eight Maids-a-Milking, ', 'nine Ladies Dancing, ', 'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ', 'twelve Drummers Drumming, ' ]
    days = range(12)
    first_half = ""
    gifts2 = ''
    trailing_gift = 'and a Partridge in a Pear Tree.'
    subresult = []
    result = []

    for i in range(s, e+1):
        for z in range(1, e+1):
            if i == 1:
                subresult = [ "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree." ]
            else:
                first_half = f"On the {prettydays[i-1]} day of Christmas my true love gave to me: "
                gifts2 = gifts[1:i]
                gifts2.reverse()
                gifts2 = ''.join(gifts2)
                subresult = [ first_half + gifts2 + trailing_gift ]
        result = result + subresult

    print(result)
    return result


recite(1,4)
