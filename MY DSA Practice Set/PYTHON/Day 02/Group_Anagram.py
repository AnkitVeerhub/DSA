'''

'''
# Brute Forec Approach
def group_anagram(strs):
    n = len(strs)
    visited = [False] * n
    result = []
    for i in range(n):
        if not visited[i]:
            group = [strs[i]]
            visited[i] = True
            for j in range(i + 1, n):
                if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            result.append(group)
    return result
strs = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab", "bac"]
print(group_anagram(strs))
# Optimal Approach
from collections import defaultdict
def group_anagram(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())
strs = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab", "bac"]
print(group_anagram(strs))  