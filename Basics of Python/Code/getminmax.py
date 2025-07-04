#Write a function get_min_max(lst) that returns the minimum and maximum of the list .
def get_min_max(lst):
    if not lst:  # Check if the list is empty
        return None, None
    min_value = lst[0]
    max_value = lst[0]
    
    for number in lst:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
            
    return min_value, max_value
# Example usage
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value, max_value = get_min_max(lst)
print("Minimum value:", min_value)
print("Maximum value:", max_value)