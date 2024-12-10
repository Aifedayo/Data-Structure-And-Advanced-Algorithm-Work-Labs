import numpy as np
import sys

def mem_test(size):
    python_list = [0] * size
    numpy_array = np.zeros(size)

    list_memory = sys.getsizeof(python_list)
    numpy_memory = numpy_array.nbytes

    print(f"Python List Memory: {list_memory} bytes")
    print(f"NumPy Array Memory: {numpy_memory} bytes")

print(mem_test(10**6))      