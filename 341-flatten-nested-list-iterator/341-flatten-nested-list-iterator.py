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
        self.answer = []
        self.dfs(nestedList)
        self.index = -1
    def dfs(self, nestedList):
        for x in nestedList:
            if x.isInteger():
                self.answer.append(x.getInteger())
            elif x.getInteger() is not None:
                self.answer.append(x.getInteger())
            else:
                self.dfs(x.getList())
    def next(self) -> int:
        self.index += 1
        return self.answer[self.index]
    def hasNext(self) -> bool:
         return self.index + 1 < len(self.answer)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())