import bisect

# Doğrusal Arama (Linear Search) - O(n)
def linear_search(arr, target):
    for i in arr:                  # O(n)
        if i == target:
            return True
    return False

# Binary Arama (Binary Search) - O(log n), sadece sıralı dizilerde
def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)  # O(log n)
    return index < len(arr) and arr[index] == target


# Test Dizisi
data = [3, 5, 8, 11, 15, 19, 24, 31, 42, 56]

# Test Aramaları
print("Linear Search (11):", linear_search(data, 11))  # True
print("Binary Search (11):", binary_search(data, 11))  # True

print("Linear Search (99):", linear_search(data, 99))  # False
print("Binary Search (99):", binary_search(data, 99))  # False
