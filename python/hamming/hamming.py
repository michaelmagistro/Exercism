def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same length")
    else:
        length = len(strand_a)
        diff = 0
        for i in range(length):
            if strand_a[i] != strand_b[i]:
                diff += 1
            else:
                continue
        return diff

