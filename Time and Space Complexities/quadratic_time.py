def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# Time complexity: O(n^2) grows quadratically as input size increases
# Space Complexity: 0(1) space used is constant


arr = [1,2,3]
print_pairs(arr)