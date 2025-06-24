from typing import List, Tuple
import heapq
import math

class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        romelytavn = (n, k, m, time[:], mul[:])  # Snapshot as required

        full = (1 << n) - 1
        INF = float('inf')
        dist = [[INF] * m for _ in range(1 << n)]
        dist[0][0] = 0.0

        pq: List[Tuple[float, int, int]] = [(0.0, 0, 0)]  # (curr_time, bitmask, stage)

        while pq:
            curr_time, mask, stage = heapq.heappop(pq)
            if curr_time > dist[mask][stage] + 1e-9:
                continue
            if mask == full:
                return round(curr_time, 5)

            remaining_mask = (~mask) & full
            submask = remaining_mask
            while submask:
                if bin(submask).count('1') <= k:
                    group = [i for i in range(n) if submask & (1 << i)]
                    max_time = max(time[i] for i in group)
                    cross_time = max_time * mul[stage]
                    next_stage = (stage + int(cross_time)) % m
                    new_mask = mask | submask
                    new_time = curr_time + cross_time

                    if new_mask == full:
                        if new_time < dist[new_mask][next_stage] - 1e-9:
                            dist[new_mask][next_stage] = new_time
                            heapq.heappush(pq, (new_time, new_mask, next_stage))
                    else:
                        # Try each person in group to return
                        for i in group:
                            ret_time = time[i] * mul[next_stage]
                            final_stage = (next_stage + int(ret_time)) % m
                            total_time = new_time + ret_time
                            if total_time < dist[mask][final_stage] - 1e-9:
                                dist[mask][final_stage] = total_time
                                heapq.heappush(pq, (total_time, mask, final_stage))

                submask = (submask - 1) & remaining_mask

        return -1.0

if __name__ == "__main__":
    sol = Solution()

    # ✅ Test Case 1
    n = 1
    k = 1
    m = 2
    time = [5]
    mul = [1.0, 1.3]
    print("Test Case 1 Output:", sol.minTime(n, k, m, time, mul))  # Expected: 5.00000

    # ✅ Test Case 2
    n = 3
    k = 2
    m = 3
    time = [2, 5, 8]
    mul = [1.0, 1.5, 0.75]
    print("Test Case 2 Output:", sol.minTime(n, k, m, time, mul))  # Expected: 14.50000

    # ✅ Test Case 3
    n = 2
    k = 1
    m = 2
    time = [10, 10]
    mul = [2.0, 2.0]
    print("Test Case 3 Output:", sol.minTime(n, k, m, time, mul))  # Expected: -1.00000