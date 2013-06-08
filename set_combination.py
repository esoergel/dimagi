def get_combinations(word_lists):
    """
    generates a list of lists of possible combinations by recursing
    on the remaining lists (yo dawg...).
    """
    if len(word_lists) == 1:
        return [ [word] for word in word_lists[0] ]

    combos = []
    sub_combos = get_combinations(word_lists[1:])

    for word in word_lists[0]:
        for sub_combo in sub_combos:
            combos.append( [word] + sub_combo )
    return combos


def print_combinations(word_lists):
    """
    Returns all possible combinations of one word from each list
    word_lists should be a list of word lists
    """
    for combination in get_combinations(word_lists):
        print " ".join(combination)


word_lists = [
    ["apple", "banana", "pear"],
    ["car", "truck"],
    ["zambia", "malawi", "kenya"],
]

print_combinations(word_lists)