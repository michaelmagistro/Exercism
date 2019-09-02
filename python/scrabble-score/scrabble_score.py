def score(word):
    letters = ['AEIOULNRST', 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'QZ']
    points = [1, 2, 3, 4, 5, 8, 10]
    score_brackets = len(points)
    score = 0
    for i in word:
        for j in range(score_brackets):
            if i.lower() in letters[j].lower(): score += points[j]
    return score
