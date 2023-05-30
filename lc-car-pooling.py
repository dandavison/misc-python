# https://leetcode.com/problems/car-pooling


# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where
# trip[i] = [numPassengers_i, from_i, to_i]
# indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for _, delta in _get_events(trips):
            n += delta
            assert n >= 0
            if n > capacity:
                return False
        return True
        
        
def _get_events(trips):
    """
    Return sorted list of (location, delta) tuples
    """
    events = []
    for n, _from, _to in trips:
        events.append((_from, n))
        events.append((_to, -n))
    return sorted(events)
