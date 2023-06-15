# You are given two 0-indexed integer arrays servers and tasks of lengths n and m respectively. servers[i] is the weight of the ith server, and tasks[j] is the time needed to process the jth task in seconds.
# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.
# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.
# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.
# A server that is assigned task j at second t will be free again at second t + tasks[j].
# Build an array ans of length m, where ans[j] is the index of the server the jth task will be assigned to.
# Return the array ans.
from collections import deque
from heapq import heappush, heappop
from typing import List

def task_assignments(servers: List[int], tasks: List[int]) -> List[int]:

    # Initialize servers heap
    servers_heap = []
    for i, weight in enumerate(servers):
        heappush(servers_heap, (weight, i))

    # Initialize task heap
    task_heap = [] # items are (task_time, server_weight, server_idx)
    # for task in tasks:
    #     heappush(task_heap, task)

    curr_time = 0

    for task in tasks:
        if (servers_heap is empty)
            curr_time = task_heap.peek()[2] # skip forward
        while task_heap:
            task_time, server_weight, server_idx = task_heap.pop()
            if task_time <= curr_time:
                heappush(servers_heap, (server_weight, server_idx))
            else:
                heappush(task_heap, (task_time, server_weight, server_idx))
                # break?

        (server_weight, server_idx) = heappop(servers_heap)
        heappush(task_heap, (task, server_weight, server_idx))
        ans.append(server_idx)
        curr_time += 1















def task_assignments_0(servers: List[int], tasks: List[int]) -> List[int]:
    """
    1. Build a min heap containing (weight, index, time_available=0) pairs representing all servers

    2. set curr_time = 0, create a queue (deque) holding the tasks

    3. While there are unassigned tasks:
          pop next server out of the heap
          // for every server that has time_available <= curr_time, we assign the next task
    """
    tasks_q = deque(tasks)

    # Initialize servers heap
    servers_heap = []
    for i, weight in enumerate(servers):
        heappush(servers_heap, (weight, i, 0))

    curr_time = 0
    ans = []
    while tasks_q:
        unavailable = []
        while servers_heap:
            (weight, i, when_available) = heappop(servers_heap)
            if when_available > curr_time:
                unavailable.append((weight, i, when_available))
            else:
                if tasks_q:
                    task  = tasks_q.popleft()
                    unavailable.append((weight, i, curr_time + task))
                    ans.append(i)
                else:
                    return ans
        for server in unavailable:
            heappush(servers_heap, server)

    return ans






# Example 1:
# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

# Example 2:
# Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# Output: [1,4,1,4,1,3,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 1 until second 2.
# - At second 1, task 1 is added and processed using server 4 until second 2.
# - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4.
# - At second 3, task 3 is added and processed using server 4 until second 7.
# - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9.
# - At second 5, task 5 is added and processed using server 3 until second 7.
# - At second 6, task 6 is added and processed using server 2 until second 7.
