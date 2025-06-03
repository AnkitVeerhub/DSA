def find_two_unique_elements(A):
    # Step 1: XOR all elements in the array
    xor_all = 0
    for num in A:
        xor_all ^= num  # This gives a ^ b (XOR of the two unique numbers)
    
    # Step 2: Find the rightmost set bit in xor_all
    diff_bit = xor_all & -xor_all
    
    # Step 3: Split the array into two groups based on diff_bit
    a = 0  # XOR of elements in the first group
    b = 0  # XOR of elements in the second group
    for num in A:
        # Group 1: XOR numbers where diff_bit is set (i.e., the current bit is 1)
        if num & diff_bit:
            a ^= num
        # Group 2: XOR numbers where diff_bit is NOT set (i.e., the current bit is 0)
        else:
            b ^= num
    
    # Step 4: Return the two unique elements
    return [a, b]
