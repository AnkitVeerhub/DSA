'''
Q1. Cycle in Directed Graph
Problem Description
Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].
Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.
NOTE:
The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
Problem Constraints
2 <= A <= 105
1 <= M <= min(200000,A*(A-1))
1 <= B[i][0], B[i][1] <= A
Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



Output Format

Return 1 if cycle is present else return 0.



Example Input

Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
Explanation 2:

 The given graph doesn't contain any cycle.
'''

from collections import defaultdict

def has_cycle(A, B):
    # Build the graph
    graph = defaultdict(list)
    for u, v in B:
        graph[u].append(v)

    visited = [False] * (A + 1)
    recStack = [False] * (A + 1)

    def dfs(node):
        visited[node] = True
        recStack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[node] = False
        return False

    # Check every component (graph may be disconnected)
    for i in range(1, A + 1):
        if not visited[i]:
            if dfs(i):
                return 1  # Cycle found

    return 0  # No cycle

# === Test case ===
A = 4
B = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 2]  # back edge creates cycle
]

result = has_cycle(A, B)
print("Cycle Detected:" if result == 1 else "No Cycle")


from collections import defaultdict

def has_cycle(A, B):
    graph = defaultdict(list)

    # ✅ Step 1: Build the graph
    for u, v in B:
        graph[u].append(v)

    # ✅ Step 2: Initialize visited and recStack outside the loop
    visited = [False] * (A + 1)
    recStack = [False] * (A + 1)

    # ✅ Step 3: Define DFS function
    def dfs(node):
        visited[node] = True
        recStack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[node] = False
        return False

    # ✅ Step 4: Run DFS for all components
    for i in range(1, A + 1):
        if not visited[i]:
            if dfs(i):
                return 1  # Cycle found

    return 0  # No cycle

# === Test case ===
A = 4
B = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 2]  # back edge creates cycle
]

result = has_cycle(A, B)
print("Cycle Detected:" if result == 1 else "No Cycle")

