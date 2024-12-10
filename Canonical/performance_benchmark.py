import numpy as np
import time

python_list = list(range(10**6))
numpy_array = np.array(range(10**6))

def performance_benchmark():
    start_time = time.perf_counter()
    python_result = [x + 1 for x in python_list]
    end_time = time.perf_counter()

    list_time = end_time - start_time


    start_time = time.perf_counter()
    numpy_result = numpy_array + 1
    end_time = time.perf_counter()
    arr_time = end_time - start_time

    print(f"Python List Time: {list_time:.6f} seconds")
    print(f"NumPy Array Time: {arr_time:.6f} seconds")


print(performance_benchmark())