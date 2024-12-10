import array
import numpy as np

def identify_ds(ds_type):
    if isinstance(ds_type, list):
        return "Python List"
    elif isinstance(ds_type, array.array):
        return "Array from `array` module"
    elif isinstance(ds_type, np.ndarray):
        return "NumPy Array"
    else:
        return "Unknown Data Structure"
    


print(identify_ds([1, 2, 3]))  # Output: Python List
print(identify_ds(array.array('i', [1, 2, 3])))  # Output: Array from `array` module
print(identify_ds(np.array([1, 2, 3])))  # Output: NumPy Array