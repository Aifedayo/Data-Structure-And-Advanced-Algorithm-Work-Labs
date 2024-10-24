def longest_distinct_substring(s, k):
    char_count = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        print(char_count)

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left+1)
    return max_length


print(longest_distinct_substring(s='akeeemm', k=2))
