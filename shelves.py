"""
In a paint shop are tins of paint. Each tin has a number. The shop has some shelves.
When a tin is placed on the shelves, the tins must be kept in order.

Each shelf fits 3 tins. The shelves are numbered starting at 1.

Your task is to write a class representing the shelves. The class should have two methods:

add_tin(tin)    # puts `tin` on the shelves
get_shelf(tin)  # returns the number of the shelf on which `tin` is located
"""

class Shelves:
    shelf_length = 2

    def __init__(self):
        self.tins = []

    def add_tin(self, tin):
        pos = 0
        for t in self.tins:
            if t > tin:
                break
            pos += 1
        self.tins = self.tins[:pos] + [tin] + self.tins[pos:]

    def get_shelf(self, tin):
        return 1 + sum(1 for t in self.tins if t <= tin) // self.shelf_length


shelves = Shelves()
shelves.insert(3)
print(shelves.tins)
shelves.insert(1)
print(shelves.tins)
shelves.insert(2)
print(shelves.tins)
shelves.insert(7)
print(shelves.tins)
shelves.insert(2)
print(shelves.tins)
shelves.insert(5)
print(shelves.tins)
shelves.insert(4)
print(shelves.tins)
print(shelves.get_shelf(4))
