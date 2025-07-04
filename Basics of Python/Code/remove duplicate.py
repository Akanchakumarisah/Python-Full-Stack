def remove_duplicates(data, key):
    seen = set()
    unique_data = []
    for item in data:
        value = item.get(key)
        if value not in seen:
            seen.add(value)
            unique_data.append(item)
    return unique_data

# Example usage
data = [
    {"id": 1, "name": "Alice"}, 
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Charlie"}, 
    {"id": 3, "name": "Alice"}
]

result = remove_duplicates(data, "id")
print(result)
