import numpy as np

def rle_encode(arr):
    change_indices = np.where(np.diff(arr) != 0)[0]+1
    
    run_lengths = np.diff(np.concatenate(([0], change_indices, [len(arr)])))
    values = arr[np.concatenate(([0], change_indices))]
    
    return run_lengths, values



# Example usage:
arr = np.array([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 2])
encoded_lengths, encoded_values = rle_encode(arr)
print("Encoded lengths:", encoded_lengths)
print("Encoded values:", encoded_values)

