# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = list(self.oneD(nestedList))
        self.idx = 0
    
    def next(self) -> int:
        if self.hasNext():
            val = self.gen[self.idx]
            self.idx += 1
        else:
            raise Exception("No more integers")
        return val
    
        
    def hasNext(self) -> bool:
        return len(self.gen) > self.idx
         
    def oneD(self, nums):
        for num in nums:
            if num.isInteger():
                yield num.getInteger()
            else:
                yield from self.oneD(num.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())