def longest_subtring(s):
    char_set = set()
    left, right = 0, 0
    max_length = 0

    while right < len(s):
        if s[right] in char_set:
            char_set = set()
        char_set.add(s[right])
        right += 1
        max_length = max(max_length, len(char_set))

    return max_length


print(longest_subtring("bbbbb"))