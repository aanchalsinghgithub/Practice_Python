# 1. find Largest Element in an Array

def largest(arr):
    return max(arr)

# print(largest([5,2,9,11,7]))

# 2.Find Smallest Element

def smallest(arr):
    return min(arr)

# print(smallest([5,2,9,1,7]))

#3. Sum of Array

def array_sum(arr):
    return sum(arr);

# print(array_sum([1,2,3,4]))

#4. Averay of Array

def average(arr):
    return sum(arr)/len(arr)

# print(average([2,4,6,8]))

# 5. Count Elements
def count_elements(arr):
    return len(arr)

# print(count_elements([1,2,3,4]))

#Check if Element Exists

def exists(arr,target):
    return target in arr

# print(exists([1,2,3,4,5], 5))

# Find Index of Element

def find_index(arr, target):
    return arr.index(target)

# print(find_index([10,20,30,40], 30))

#Reverse an Array

def reverse_array(arr):
    return arr[::-1]

# print(reverse_array([1,2,3,4]))

# Sort Array Ascending
def sort_array(arr):
    return sorted(arr)

# print(sort_array([5,1,4,2]))

# Sort Array Descending

def sort_desc(arr):
    return sorted(arr,reverse=True)

# print(sort_desc([1,5,2,3]))

# Find Maximum and Minimum

def max_min(arr):
    return max(arr), min(arr)

print(max_min([5,2,8,1]))





