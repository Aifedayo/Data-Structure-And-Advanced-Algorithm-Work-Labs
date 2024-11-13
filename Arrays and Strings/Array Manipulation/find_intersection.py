def find_intersection(arr1, arr2):
    arr1 = set(arr1[0].split(", "))
    arr2 = set(arr2[0].split(", "))

    return list(arr1 & arr2)


print(find_intersection(["1, 2, 3, 4"], ["2, 4, 6, 8"]))