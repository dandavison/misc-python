# https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        return zip(*reversed(shift(box)))
    

def shift(box):
    for row in box:
        shift_row(row)
    return box

        
def shift_row(row):
    next_obstacle = 0
    for i in range(len(row)):
        idx = -(i+1)
        if row[idx] == "#":
            # Shift stone rightward
            row[idx]  = "." 
            row[next_obstacle - 1] = "#"
            next_obstacle -= 1
        elif row[idx] == "*":
            next_obstacle = idx            
        
if False:
    def transpose(box):
        if not box:
            return box
        transposed = []
        for j in range(len(box[0])):
            row = [box[i][j] for i in range(len(box))]
            transposed.append(row)
        return transposed
