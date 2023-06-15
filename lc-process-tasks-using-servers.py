# https://leetcode.com/problems/process-tasks-using-servers/

# You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

# A server that is assigned task j at second t will be free again at second t + tasks[j].

# Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

# Return the array ans​​​​.
from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        Essentially we want to do:

        while (there are tasks):
            (assign next task to a server)

        We'll maintain two partitions of the servers: those available now, and those processing tasks.

        We'll use a min-heap for both:
        available now: retrieve first according to priority criteria
        processing tasks: retrieve next one to become available

        Thus:

        1. Insert all servers into available_now heap.

        2. Set curr_time = 0

        3. For each task:
               If there's an available server then assign it.
               Otherwise:
                   Advance to time when next server becomes available.
                   Assign it.
        """
        # Initialize available heap
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapify(available)

        # Initialize busy heap
        busy = []

        ans = []
        curr_time = 0
        for task_idx, task_duration in enumerate(tasks):

            # If none are available or have become free, then fast-forward
            if not available and busy and busy[0][0] > curr_time:
                curr_time = busy[0][0]

            # Free up servers that have finished their tasks
            while busy and busy[0][0] <= curr_time:
                _, server_weight, server_idx = heappop(busy)
                heappush(available, (server_weight, server_idx))

            # Assign the task to a server
            server_weight, server_idx = heappop(available)
            ans.append(server_idx)
            heappush(busy, (curr_time + task_duration, server_weight, server_idx))
            curr_time = max(curr_time, task_idx + 1)

        return ans
