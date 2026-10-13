def sort_ascending(numbers):
    return sorted(numbers)


def sort_descending(numbers):
    return sorted(numbers, reverse=True)


numbers = [5, 2, 9, 1, 7]

print("Ascending:", sort_ascending(numbers))
print("Descending:", sort_descending(numbers))
