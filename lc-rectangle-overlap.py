"""
https://leetcode.com/problems/rectangle-overlap/

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1,
y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate
of its top-right corner. Its top and bottom edges are parallel to the X-axis,
and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be
clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap,
otherwise return false.
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1, b1, r1, t1 = rec1
        l2, b2, r2, t2 = rec2
                
        horiz_separated = r1 <= l2 or r2 <= l1
        vert_separated = t1 <= b2 or t2 <= b1
        return not (horiz_separated or vert_separated)
