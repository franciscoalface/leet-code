def group_anagrams(strs):
    result = []
    anagrams = {}

    for s in strs:
        hashed = "".join(sorted(s))
        if hashed not in anagrams:
            anagrams[hashed] = []
        anagrams[hashed].append(s)

    for a in anagrams.values():
        result.append(a)

    return result
