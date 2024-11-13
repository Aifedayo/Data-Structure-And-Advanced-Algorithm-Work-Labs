def longest_word(sen):
    words = [word.strip('.,!?') for word in sen.split()]
    return max(words, key=len)


print(longest_word('The quick brown fox jumps ver the lazy dog'))