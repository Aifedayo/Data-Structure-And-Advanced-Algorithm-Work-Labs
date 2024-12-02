"""
Let’s move to string manipulation, another essential topic for Python interviews.

Concept: Adding Large Numbers Represented as Strings
When numbers are too large to fit in standard data types, they are often represented as strings. 
Your task is to perform operations like addition on these string numbers.
"""

"""
Example Problem
Write a function to add two numbers represented as strings.

Input:
num1 = "12345"
num2 = "6789"

Output:
"19134"
"""


def large_num_str(num1, num2):
    left, right = 0, 0
    result = ''

    reversed_num1 = num1[::-1]
    reversed_num2 = num2[::-1]
    carry = 0

    while left < len(reversed_num1) or right < len(reversed_num2) or carry > 0:
        digit1 = int(reversed_num1[left]) if left < len(reversed_num1) else 0
        digit2 = int(reversed_num2[right]) if right < len(reversed_num2) else 0


        operation = digit1 + digit2 + carry
        carry = operation // 10
        value = operation % 10
        result += str(value)

        left += 1
        right += 1

    return result[::-1]

num1 = "12345"
num2 = "6789"
print(large_num_str(num1, num2))
