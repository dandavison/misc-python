class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        a = {
            "x": [ax1, ax2],
            "y": [ay1, ay2]
        }
        b = {
            "x": [bx1, bx2],
            "y": [by1, by2]
        }
        return area(a) + area(b) - intersection(a, b) 


def intersection(a, b):
    # horiz
    starts = a["x"][0], b["x"][0]
    ends = a["x"][1], b["x"][1]
    horiz_intersection = max(min(ends) - max(starts), 0)
    
    
    # vert
    starts = a["y"][0], b["y"][0]
    ends = a["y"][1], b["y"][1]
    vert_intersection = max(min(ends) - max(starts), 0)
    
    return horiz_intersection * vert_intersection
        

def area(a):
    return (a["x"][1] - a["x"][0]) * (a["y"][1] - a["y"][0])
