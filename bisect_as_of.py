import bisect
from datetime import datetime
from functools import total_ordering


class Store:
    def __init__(self):
        self.events = {}
        self.sentinel = Sentinel()

    def put(self, key, value):
        timestamp = datetime.utcnow().timestamp()
        self.events.setdefault(key, []).append(Event(value, timestamp))
    
    def get(self, key):
        now = datetime.utcnow().timestamp()
        return self.get_as_of(key, now)

    def get_as_of(self, key, timestamp):
        key_events = self.events[key]
        idx = bisect.bisect(key_events, Event(None, timestamp))
        if idx == 0:
            raise KeyError("Requested timestamp must post-date key creation")
        ts, value = key_events[idx - 1]
        return value


@total_ordering
class Event:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp


@total_ordering
class Sentinel:
    def __lt__(self, other):
        return False



#           <---- query before create: KeyError: No value <= t
# create t1
# update t2
#           <---- query t: we want index 1: want index of rightmost value that is <= t 
# update t3
