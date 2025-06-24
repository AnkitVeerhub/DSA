'''
3443. Maximum Manhattan Distance After K
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.
'''

def max_manhattan_distance_with_k_changes(s,k):
    x,y,max_dist = 0,0,0
    N_count,E_count, W_count, S_count = 0, 0, 0, 0
    for i in s:
        if i == 'N':
            y += 1
            N_count += 1
        elif i == 'S':
            y -= 1
            S_count += 1
        elif i == 'E':
            x += 1
            E_count += 1
        elif i == 'W':
            x -= 1
            W_count += 1
        # Greedily enhance distance with upto k flip
        potential_x = abs(x) + min(k, W_count) * 2
        potential_y = abs(y) + min(k , S_count) * 2
        enhance_dis = potential_x + potential_y
        max_dist = max(max_dist, enhance_dis)
    return max_dist
print(max_manhattan_distance_with_k_changes("NENWS", 1))  # Example: Should be greater than 2
