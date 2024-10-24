def longest_distinct_substring(s, k):
    curr_window = ''
    max_length = 0
    left = 0

    for right in range(len(s)):
        curr_window += s[right]

        while len(set(curr_window)) > k:
            curr_window = s[left+1:right+1]
            left += 1

        max_length = max(max_length, right - left+1)
    return max_length


print(longest_distinct_substring(s='akeeem', k=2))