'''
🧩 Painter Partition Problem
📌 Problem Statement (LeetCode-style):
You are given:

An array boards[], where each element represents the length of a board.

k painters available.

boards = [10, 20, 30, 40]
k = 2
We can split the boards into:

[10, 20, 30] → total = 60

[40] → total = 40
→ Max time = 60

Another way:

[10, 20] → total = 30

[30, 40] → total = 70
→ Max time = 70 ❌ worse

✅ So, 60 is the minimum possible max time.
'''
def painter_partition(boards, k):
    def canPaint(max_time):
        painter_count, current_time = 1, 0
        for length in boards:
            if current_time + length > max_time:
                painter_count += 1
                current_time = length
            else:
                current_time += length
        return painter_count <= k
    low, high = max(boards), sum(boards)
    answer = high
    while low <= high:
        mid = (low + high)//2
        if canPaint(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer
boards = [10, 20, 30, 40]
k = 2
print(painter_partition(boards, k))

    
# Painter Partion minimum time required Optimal Approach
def min_time_required(A,B,C):
    def canPaint(time_limit):
        painters, total_time = 1, 0
        for length in C:
            total_time += length * B
            if total_time > time_limit:
                painters += 1
                total_time = length * B
                if painters > A:
                    return False
        return True
    if A >= len(C):
        return (max(C) * B) % 10000003
    low, high = max(C) * B, sum(C) * B
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if canPaint(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer
A = 2  # Number of painters
B = 5  # Time per unit length
C = [1, 10]  # Lengths of boards

print(min_time_required(A,B,C))