def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq

# Time complexity: O(n)
# Space complexity: O(n)
