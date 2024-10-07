def count_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

# Time complexity: O(n)
# Space complexity: O(n)
