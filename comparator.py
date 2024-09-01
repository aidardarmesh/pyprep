ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ch', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z'
]

ALPHABET_ORDER = {ch: i for i, ch in enumerate(ALPHABET)}

def custom_comparator(word):
    res, n, i = [], len(word), 0

    while i < n:
        if word[i] == 'c':
            if i+1 < n and word[i+1] == 'h':
                res.append(ALPHABET_ORDER['ch'])
                i += 2
                continue
        res.append(ALPHABET_ORDER[word[i]])
        i += 1
    
    return tuple(res)


tests = [
    ["indigo", "charisma", "hotel"],
    ["indigo", "charisma", "hotel", "charis"],
    ["ahac", "achb"],
    ["ab", "abc", "a"]
]

for test in tests:
    test.sort(key=custom_comparator)
    print(test)
