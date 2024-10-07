def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Time complexity: 0(n) Because we loop through once, algo run time gets bigger per input size

# Space complexity: 0(n): The space grows linearly in size with each input