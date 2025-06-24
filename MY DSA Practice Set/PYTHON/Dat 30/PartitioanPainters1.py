'''
Given N board with length of each board.
(a). A Painter takes T unit of time to paint 1 unit of length
(b). A board can only be painted by 1 painter
(C). A painter can only paint boards placed next to each other (i.e.: continous segment)
Q. Find the minimum number of painters required to to print all boards in x unit of time.
   Retuen -1 if not possible.
'''


# Brute Force Approach/Optimal Approach
def minimum_painter_required(T, X, A):
    painter = 1
    time_left = X
    for i in range(len(A)):
        if A[i]*T > X:
            return -1
        if A[i]*T <= time_left:
            time_left = time_left - A[i] * T
        else:
            painter += 1
            time_left = X - A[i] * T
    return painter
T = 2
X = 20
A = [5, 3, 6, 1, 9]
print(minimum_painter_required(T,X,A))
