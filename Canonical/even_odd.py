"""
Given an array called an_array of non_negative int, return an array  consisting of all the even elements
of an_array, followed by all the odd elements of an_array
"""

def even_then_odd(an_array):
    even = 0
    for i in range(len(an_array)):
        if an_array[i] % 2 == 0:
            an_array[i], an_array[even] = an_array[even], an_array[i]
            even += 1

    return an_array

print(even_then_odd([2,3,4,5,6,7,8,9])) 