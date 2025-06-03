'''
Find Nearest Smallest Element - Stack
'''

def nearest_smalest_element(A):
    n = len(A)
    result = []
    for i in range(n):
        smaller = -1
        for j in range(i-1,-1,-1):
            if A[j] < A[i]:
                smaller = A[j]
                break
        result.append(smaller)
    return result
print(nearest_smalest_element([4, 5, 2, 10, 8]))

def nearest_smaller_elements(arr):
    n = len(arr)             # Get the length of the array
    result = []              # This will store our final result

    for i in range(n):       # Loop over each element in the array
        found = False        # Flag to check if a smaller element is found

        # Check all elements to the left of current element (i - 1 to 0)
        for j in range(i - 1, -1, -1):  # Reverse loop: start from i-1 down to 0
            if arr[j] < arr[i]:        # If a smaller element is found
                result.append(arr[j])  # Add it to the result
                found = True           # Mark that we found one
                break                  # Exit the inner loop early

        if not found:
            result.append(-1)  # If no smaller element found, append -1

    return result             # Return the list of nearest smaller elements
print(nearest_smaller_elements([4, 5, 2, 10, 8]))


# Using Stack
def nearest_smallest_element_stack(A):
    n = len(A)
    stack = []
    result = []
    for i in range(n):
        while stack and stack[-1] >= A[i]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(A[i])
    return result
print(nearest_smallest_element_stack([4, 5, 2, 10, 8]))
