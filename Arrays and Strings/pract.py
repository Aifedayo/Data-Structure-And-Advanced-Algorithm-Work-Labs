def find_majority_element(arr):

    hashfreq = {}

    for num in arr:
        hashfreq[num] = hashfreq.get(num, 0) + 1

    maj_element = max(hashfreq, key=hashfreq.get)
    return maj_element
        

print(find_majority_element([1,1,2,4,5,5,5,5]))