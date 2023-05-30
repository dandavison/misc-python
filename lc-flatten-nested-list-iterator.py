# https://leetcode.com/problems/flatten-nested-list-iterator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from itertools import chain


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iterator = make_iterator(nestedList)

    def next(self) -> int:
        return next(self.iterator)

    def hasNext(self) -> bool:
        try:
            el = next(self.iterator)
        except StopIteration:
            return False
        else:
            self.iterator = chain([el], self.iterator)
            return True


def make_iterator(nestedList):
    for ni in nestedList:
        if ni.isInteger():
            yield ni.getInteger()
        else:
            yield from make_iterator(ni.getList())


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
