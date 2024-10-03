import numpy as np 

def numpy_operations() ->dict:
    original_array = np.array([1,2,3,4,5])
    modified_array =original_array +10
    mean_of_original=np.mean(original_array)

    result={
        "modified_array":modified_array,
        "mean_of_original":mean_of_original
    }

    return result
