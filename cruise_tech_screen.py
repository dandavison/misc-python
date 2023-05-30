"""
Given a sequence of closed time intervals which could be overlapping, find the range that has the maximum overlap. 

Examples:
[1,3] [2,9] ----> [2,3]  ( Between [2,3] both the intervals overlap )
As ASCII art:
0 1 2 3 4 5 6 7 8 9 
  - - -
      - - -
  1 1 2 1 1
  
      
    - - - - - - - -
            - - -
                - 
                * [8,8]


[1,5] [2,8] [4,12] ----> [4,5] (Between [4,5] all three intervals overlap)
[1,3] [4,7] [9,13] -----> [1,3] || [4,7] || [9,13] (In this case, there is no overlap, so either range is acceptable)
[1,5] [9,11] [2,8] [4,12] ----> [4,5] (Between [4,5], three intervals overlap)

Constraints:
1. Maximum overlap is defined as that range which has the most number of overlapping intervals. 
2. If the maximum overlap has more than one solution, you can return any one of the intervals.
3. The intervals could be specified in any order. 
4. The interval start/end times could be any positive integer between 0 to 2^32-1.
5. The number of intervals will not exceed 1 million.

"""
from typing import List, Tuple

def find_maximum_overlap_interval(intervals: List[Tuple[int, int]]):

    events = get_events(intervals)

    max_start, max_end, maximum = object(), object(), None
    
    overlap = 0
    for (position, value) in events:
        overlap += value
                
        if maximum is None or overlap > maximum:
            maximum = overlap
            max_start = position
            max_end = None
        elif maximum is not None and overlap < maximum and max_end is None:
            max_end = position            
                        
    return (max_start, max_end - 1)
        
    
def get_events(intervals):
    """
    Return ordered list of "events"
    """
    events = []
    for (start, end) in intervals:
        events.append((start, 1))
        events.append((end + 1, -1))
    return sorted(events)


print(find_maximum_overlap_interval([[1,3], [2,9]])) #  ----> [2,3]
print(find_maximum_overlap_interval([[1,5], [2,8], [4,12]])) #  ----> [4, 5]