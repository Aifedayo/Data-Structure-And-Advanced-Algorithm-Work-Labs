from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t) # Number of uniue characters in t

    left, right = 0, 0

    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < ans[0]:
                ans