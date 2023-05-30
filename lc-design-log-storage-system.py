# https://leetcode.com/problems/design-log-storage-system


# You are given several logs, where each log contains a unique ID and timestamp.
# Timestamp is a string that has the following format:
# Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All
# domains are zero-padded decimal numbers.

# Implement the LogSystem class:

# LogSystem() Initializes the LogSystem object.

# void put(int id, string timestamp)
#
# Stores the given log (id, timestamp) in your storage system.

# int[] retrieve(string start, string end, string granularity)
#
# Returns the IDs of the logs whose timestamps are within the range from start
# to end inclusive. start and end all have the same format as timestamp, and
# granularity means how precise the range should be (i.e. to the exact Day,
# Minute, etc.). For example, start = "2017:01:01:23:59:59", end =
# "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the
# logs within the inclusive range from Jan. 1st 2017 to Jan. 2nd 2017, and the
# Hour, Minute, and Second for each log entry can be ignored.


class LogSystem:
    def __init__(self):
        self.logs = []
        self.granularities = {
            gran: index
            for index, gran in enumerate(
                ["Year", "Month", "Day", "Hour", "Minute", "Second"]
            )
        }

    def put(self, id: int, timestamp: str) -> None:
        ts = self._parse_timestamp(timestamp)
        self.logs.append((id, ts))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        parsed_start = self._parse_timestamp(start)
        parsed_end = self._parse_timestamp(end)
        granularity_idx = self.granularities[granularity]

        # We truncate start downwards ("floor") and end upwards ("ceil")
        parsed_end[granularity_idx] += 1

        self._truncate(parsed_start, granularity_idx)
        self._truncate(parsed_end, granularity_idx)

        output = []
        for (id, ts) in self.logs:
            if parsed_start <= ts < parsed_end:
                output.append(id)
        return output

    def _truncate(self, parsed_timestamp, granularity_idx):
        for idx in range(granularity_idx + 1, len(parsed_timestamp)):
            parsed_timestamp[idx] = 0

    def _parse_timestamp(self, timestamp: str):
        return list(map(int, timestamp.split(":")))


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
