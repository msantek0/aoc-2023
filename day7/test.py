from functools import cmp_to_key
from collections import Counter
def custom_key_comparison(key1, key2):
    """
    Custom comparison function for sorting dictionary keys.

    Args:
    - key1: The first key for comparison.
    - key2: The second key for comparison.

    Returns:
    - A negative value if key1 < key2.
    - 0 if key1 == key2.
    - A positive value if key1 > key2.
    """
    print(key1, key2)
    # You can customize the comparison logic here
    if key1 < key2:
        return 1
    elif key1 == key2:
        return 0
    else:
        return -1

# Example usage with sorted()
my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
compare = cmp_to_key(custom_key_comparison)
# Sort the dictionary based on keys using the custom comparison function
sorted_dict = dict(sorted(my_dict.items(), key=compare))

print(sorted_dict)
