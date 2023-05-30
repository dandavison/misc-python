class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort by end point.
        # Consider first such sorted ballon.
        # We must remove it via some shot; where shall we shoot?
        # Right at its end; then we eliminate all overlappers.

        points = sorted(points, key=lambda p: p[1])

        if not points:
            return 0

        (curr_start, curr_end), *points = points

        n_arrows = 1
        for start, end in points:
            if start > curr_end:
                n_arrows += 1
                curr_start, curr_end = start, end

        return n_arrows
